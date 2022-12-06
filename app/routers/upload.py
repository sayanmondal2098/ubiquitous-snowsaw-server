from typing import Union
from fastapi import APIRouter, File, UploadFile
from fastapi.params import Body
import shutil


router = APIRouter(
    prefix="/upload",
    tags=["upload"]
)


@router.get("/")
def uploadGet():
    return {"message":"Upload Get Called"}


@router.post("/files/")
async def create_file(file: Union[bytes, None] = File(default=None)):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}


@router.post("/uploadfile/")
async def create_upload_file(file: Union[UploadFile, None] = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        with open(f'{file.filename}',"wb") as buffer:
            shutil.copyfileobj(file.file,buffer)
        shutil.move(file.filename,'./downloads/'+file.filename)
        return {"filename": file.filename}
