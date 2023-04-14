from dollar import Dollar
from inflation import Inflation
from fastapi import FastAPI

app = FastAPI()

data = {}
dollar = Dollar()
inflation = Inflation()

data.update(dollar.data)
data.update(inflation.data)


@app.get('/')
def run():
    
    data = {}
    dollar = Dollar()
    inflation = Inflation()

    data.update(dollar.data)
    data.update(inflation.data)

    return data
