import os
import time
from typing import Union, Annotated
from fastapi.middleware.cors import CORSMiddleware

import uuid

from fastapi import FastAPI
from fastapi import File, Form, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from openai import OpenAI

import logging
logger = logging.getLogger(__name__)

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