from fastapi import FastAPI, File, UploadFile, Header
from typing import Optional
from imageHelper import img2encoding, isRegistered
from dbHelper1 import write, search

app = FastAPI()

@app.post("/face/v1")
async def register(type: str = Header(None), id: str = Header(None), file: UploadFile = File(...)):

    if type == 'register':
        encoding = await img2encoding(file)
        if encoding == False:
            return {"response": "No faces found!"}

        result = write(id, encoding)

        return {
            "response": result
        }
    elif type == 'lookup':
        encoding = await img2encoding(file)
        if encoding == False:
            return {"response": "No faces found!"}
        knownEnc = search(id)
        if not knownEnc:
            return { "response": "User is unregistered" }

        result = isRegistered(encoding, knownEnc)

        if result:
            return { "response": "User is authorized" } 

        return {
            "response": "User is unauthorized"
        }


