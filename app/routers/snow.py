from fastapi import routing, APIRouter, FastAPI
from ..Snowutils import get_file_attachment


router = APIRouter(
    prefix="/snow"
)


@router.get("/")
def getSnow():
    return {"message": "Hello ServiceNow"}


@router.get("/download")
def getSnowFile():
    get_file_attachment('INC0010001')
    return {"message": "Download Done"}
