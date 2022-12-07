from fastapi import routing, APIRouter, FastAPI
from ..utils.Snowutils import get_file_attachment


router = APIRouter(
    prefix="/snow",
    tags=["ServiceNow"]
)


@router.get("/")
def getSnow():
    return {"message": "Hello ServiceNow"}


@router.get("/download/{caseNo}")
def getSnowFile(caseNo):
    get_file_attachment(caseNo)
    return {"message": "Download Done"}
