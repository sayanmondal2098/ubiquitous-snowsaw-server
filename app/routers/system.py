from fastapi import APIRouter
from fastapi.params import Body
from ..utils.Sysutils import return_system_info, test, run_cmd
import json


router = APIRouter(
    prefix="/system",
    tags=["System"]
)

@router.get("/")
def getSysinfo():
    return return_system_info()
    

@router.post("/cmd")
def runCmd(payLoad : dict = Body(...)):
    return run_cmd(payLoad["cmd"])
    

