from dollar import Dollar
from inflation import Inflation
from interest import Interest
from fastapi import FastAPI

app = FastAPI()

data = {}
dollar = Dollar()
inflation = Inflation()
interest = Interest()

data.update(dollar.data)
data.update(inflation.data)
data.update(interest.data)

print(data)

"""
@app.get('/')
def run():
    
    data = {}
    dollar = Dollar()
    inflation = Inflation()

    data.update(dollar.data)
    data.update(inflation.data)

    return data
"""
