from fastapi import APIRouter
from fastapi.params import Body
from ..Sysutils import return_system_info, test, run_cmd
import json


router = APIRouter(
    prefix="/system"
)

@router.get("/")
def getSysinfo():
    return return_system_info()
    

@router.post("/cmd")
def runCmd(payLoad : dict = Body(...)):
    return run_cmd(payLoad["cmd"])
    

