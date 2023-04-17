from dollar import Dollar
from inflation import Inflation
from interest import Interest
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get('/data', response_model=dict)
def run():

    dollar = Dollar()
    inflation = Inflation()
    interest = Interest()

    data = {**dollar.data, **inflation.data, **interest.data}

    return JSONResponse(content=data)
