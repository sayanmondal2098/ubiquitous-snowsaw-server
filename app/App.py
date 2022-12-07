from typing import Union
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

from .routers import snow, system, upload

from .utils.Fileutils import archive, cleanupDirctory

app = FastAPI()


app.include_router(snow.router)
app.include_router(system.router)
app.include_router(upload.router)


@app.get("/")
def basicGet():
    res = archive('INC000001','./downloads/')
    if(res == True):
        cleanup = cleanupDirctory('./downloads/')
        if(cleanup == True):
            return {"message": "successfully zipped",
                    "cleanup": "successfully cleanedup"}
        else:
            return {"message": "error in cleanedup"}
    else:
        return {"message": "zip operation error triggered"}

@app.post("/")
def basic_post(payLoad : dict = Body(...)):
    print(payLoad)
    return {"message": f"successfull post request with data {payLoad} "}