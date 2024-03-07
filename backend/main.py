import logging
import os
import time
import uuid
from typing import Annotated, Union

from fastapi import FastAPI, File, Form, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from openai import OpenAI

logger = logging.getLogger(__name__)

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:80",
    "http://localhost",
    "https://localhost",
    "https://localhost:80",
    "https://dr-dracula-61s3.vercel.app/",
    "https://dr-dracula-leap-2024.vercel.app/",
    "https://dr-dracula.vercel.app/",
    "https://27c6-2a01-4ff-f0-380f-00-1.ngrok-free.app/",
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

@app.post("/blood-test")
async def upload_pdf(upload_file: Annotated[bytes, File()]):
    logger.info(f"Recieved file of length {len(upload_file)}")

    try:
        # check for uploads folder, if not create one
        if not os.path.exists("uploads/"):
            # Create the upload folder
            os.makedirs("uploads/")

        save_file = f"uploads/{str(uuid.uuid4())}.pdf"
        # dont have to save it locally as a file actually, just added it to test that we get the file from the frontend and I can open it properly
        with open(save_file, "wb+") as file_object:
            file_object.write(upload_file)
        
        logger.info(f"{save_file} saved")

        # add logic for extracting text from pdf and getting a dictionary
        # add logic to return the supabase pdf file of the report
        
        # set up ai assistant chat thread
        oai_client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY")
        )

        # upload PDF
        ast_file = oai_client.files.create(
            file=open(save_file, "rb"),
            purpose='assistants'
        )

        # create message thread for assistant
        ast_thread = oai_client.beta.threads.create()

        # setup message prompt
        oai_client.beta.threads.messages.create(
            thread_id=ast_thread.id,
            role="user",
            content="Please give me a report from the PDF",
            file_ids=[ast_file.id]
        )

        ast_run = oai_client.beta.threads.runs.create(
            thread_id=ast_thread.id,
            assistant_id=os.environ.get("OPENAI_ASSISTANT_ID")
        )

        ast_run_status = oai_client.beta.threads.runs.retrieve(
            thread_id=ast_thread.id,
            run_id=ast_run.id
        )

        logger.info("Sending to OpenAI assistant for processing")

        while ast_run_status.status != "completed":
            logger.info("AI processing...")
            time.sleep(10)

            ast_run_status = oai_client.beta.threads.runs.retrieve(
                thread_id=ast_thread.id,
                run_id=ast_run.id
            )

        ast_messages = oai_client.beta.threads.messages.list(
            thread_id=ast_thread.id
        )

        # get ai response
        ai_resp = ast_messages.data[0].content[0].text.value

        logger.info(f"\n ai_resp: {ai_resp}\n")

        # json response
        json_resp = {
            "file_size": len(upload_file),
            "report": ai_resp
        }
    except Exception as err:
        json_resp = {
            "file_size": 0,
            "report": "There was an error. Please try again."
        }

        logger.error(err)

    return JSONResponse(
        content=jsonable_encoder(
            json_resp
        )
    )
