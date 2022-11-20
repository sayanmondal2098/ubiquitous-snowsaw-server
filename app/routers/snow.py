from fastapi import routing, APIRouter, FastAPI

router = APIRouter(
    prefix="/snow"
)

@router.get("/")
def getSnow():
    return {"message": "Hello ServiceNow"}
