# App imports
from scrapping.dynamics.stock_market import StockMarket
from scrapping.statics.dollar import Dollar
from scrapping.statics.inflation import Inflation
from scrapping.statics.interest import Interest
# FastAPI imports
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates: object = Jinja2Templates(directory='templates')

app = FastAPI()
app.mount('/static', StaticFiles(directory="static"), name="static")


@app.get('/')
def run(request: Request):

    dollar: object = Dollar()
    inflation: object = Inflation()
    interest: object = Interest()
    stock_market: object = StockMarket()

    data: dict = {**dollar.data, **inflation.data,
                  **interest.data, **stock_market.data}

    return templates.TemplateResponse('home.html',
                                      {'request': request, 'data': data})


@app.get('/data/json')
def run_json() -> JSONResponse:

    dollar: object = Dollar()
    inflation: object = Inflation()
    interest: object = Interest()
    stock_market: object = StockMarket()

    data: dict = {**dollar.data, **inflation.data,
                  **interest.data, **stock_market.data}

    return JSONResponse(data)
