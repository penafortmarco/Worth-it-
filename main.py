from dollar import Dollar
from inflation import Inflation
from interest import Interest
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/data', response_model=dict)
def run():

    dollar = Dollar()
    inflation = Inflation()
    interest = Interest()

    data = {**dollar.data, **inflation.data, **interest.data}

    return JSONResponse(content=data)
