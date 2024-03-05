import os
from typing import Union, Annotated
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from fastapi import FastAPI, File, Form, UploadFile

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

@app.post("/blood-test")
async def upload_pdf(
    file: Annotated[bytes, File()],
    ):
    # dont have to save it locally as a file actually, just added it to test that we get the file from the frontend and I can open it properly
    with open("bloods.pdf", "wb+") as file_object:
        file_object.write(file)

    # add logic for extracting text from pdf and getting a dictionary
    
    # add logic to return the supabase pdf file of the report
    
    return {
        "file_size": len(file),
    }