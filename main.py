from fastapi import FastAPI, File, UploadFile
from s3 import *
app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    upload_file_to_s3(file)