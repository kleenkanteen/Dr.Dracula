import os
from typing import Annotated
import re

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi import FastAPI, File

import fitz
from openai import OpenAI
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def read_pdf(pdf_path: str):
    output_path = f"temp/{os.path.basename(pdf_path)}.txt"
    doc = fitz.open(pdf_path) # open a document
    out = open(output_path, "wb") # create a text output
    for page in doc: # iterate the document pages
        text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
        out.write(text) # write text of page in the output .txt file
        out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
    out.close()
    return output_path

def extract_number(input_string: str):
    """
    a simple utility function for extracting a number out of a string
    """
    match = re.search(r'\d+(\.\d+)?', input_string)
    if match:
        return float(match.group())
    else:
        return None

def contains_alphabet(input_string):
    """
    a simple utility function for checking if a string has letters from the alphabet
    """
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for char in input_string:
        if char in alphabet:
            return True
    return False

def extract_biomarker_values(test_file_path: str):
    """
    A function to check a generated .txt file for biomarkers and make the dictionaries for the blood test
    """
    initial_biomarkers = [] # create an empty list for the biomarkers
    clean_blood_test = [] # create an empty list for the test dictionaries
    with open(test_file_path, "rb") as x:
        lines = x.readlines()  # read all lines into a list
        with open("biomarkers.txt", "rb") as y:
            for biomarker in y: # loop through all lines (biomarkers) in the biomarkers file
                initial_biomarkers.append(biomarker.lower().strip().decode("UTF-8")) # add the biomarker to the list
            y.close() # close the biomarkers file as it is not needed anymore
        for i, line in enumerate(lines): # loop through all lines of the blood test txt file
            if line.lower().strip().decode("UTF-8") in initial_biomarkers:
                if i < len(lines) - 1: # if it's not the last line
                    biomarker_value = extract_number(lines[i + 1].strip().decode("UTF-8")) # getting the biomarker's tested value as a float
                    if "ratio" in line.strip().lower().decode("UTF-8"): # if it's a ratio
                        biomarker_measuring_unit = False
                        biomarker_normal_range = False
                    else:
                        biomarker_measuring_unit = lines[i + 2].strip().decode("UTF-8") # getting the biomarker's measuring unit
                        biomarker_normal_range = lines[i + 3].strip().decode("UTF-8")
                        if contains_alphabet(biomarker_normal_range):
                            biomarker_normal_range = False
                    biomarker_dict = {
                        "biomarker": line.strip().decode("UTF-8"),
                        "value": biomarker_value,
                        "measuring_unit": biomarker_measuring_unit or "%",
                        "normal_range": biomarker_normal_range or "Unknown"
                    } # create a dictionary with the tested biomarker data
                    clean_blood_test.append(biomarker_dict) # add the created dictionary to the result list
                else: # if it's the last line (unlikely case)
                    pass
        x.close() # close the test's txt file as it's not needed anymore
    return clean_blood_test

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

@app.post("/blood-test")
async def upload_pdf(
    file: Annotated[bytes, File()],
    ):
    # dont have to save it locally as a file actually, just added it to test that we get the file from the frontend and I can open it properly
    with open("temp/bloods.pdf", "wb+") as file_object:
        file_object.write(file)

    biomarker_values = extract_biomarker_values(read_pdf("temp/bloods.pdf"))

    # write biomarker_values to a local txt file 
    with open("temp/biomarker_values.txt", "w") as f:
        for item in biomarker_values:
            f.write(f"{item}\n")
    
    analysis = {}
    client = OpenAI()
    for biomarker in biomarker_values:
        medical_reference = supabase.table("biomarker_reference").select("*").eq("biomarker", biomarker['biomarker']).execute()

        query = f"""
        Context information is below.
        ---------------------
        Biomarker: {medical_reference.data[0]['biomarker']}
        About the test: {medical_reference.data[0]['about']}
        Interpretation: {medical_reference.data[0]['interpreting_result']}
        Source: {medical_reference.data[0]['source']}
        ---------------------
        Given the context information and not prior knowledge, answer the query.
        Query: Here is a biomarker:{biomarker['biomarker']}. The test result is {biomarker['value']} {biomarker['measuring_unit']}. The normal range is {biomarker['normal_range']}.
        Answer: 
        """

        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a medical doctor who is adept at reading blood tests and giving concise explanations."},
                {"role": "user", "content": f"Here is a biomarker:{biomarker['biomarker']}. The test result is {biomarker['value']} {biomarker['measuring_unit']}. The normal range is {biomarker['normal_range']}. Using the following information, explain what the test is about and if the. "},
            ],
            model="gpt-3.5-turbo",
        )



    
    return {
        "file_size": len(file),
        "biomarker_values": biomarker_values,
    }
