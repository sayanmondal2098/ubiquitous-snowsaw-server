from typing import Union
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

from .routers import snow, system

app = FastAPI()


app.include_router(snow.router)
app.include_router(system.router)


@app.get("/")
def basicGet():
    return {"message": "Hello World"}

@app.post("/")
def basic_post(payLoad : dict = Body(...)):
    print(payLoad)
    return {"message": f"successfull post request with data {payLoad} "}