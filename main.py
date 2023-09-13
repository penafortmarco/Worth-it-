from database.query import Query
from utils.pdf_generator import generate_pdf
# FastAPI imports
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.responses import StreamingResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from io import BytesIO

templates: object = Jinja2Templates(directory='templates')

app = FastAPI()
app.mount('/static', StaticFiles(directory="static"), name="static")


@app.get('/')
def run(request: Request):

    query = Query()
    data: dict = query.data_query()

    return templates.TemplateResponse('main.html',
                                      {'request': request, 'data': data})


@app.get('/report')
def generate_report(request: Request, dollar: bool = False, inflation: bool = False,
                    interest: bool = False, stock_market: bool = False,
                    crypto: bool = False):

    if (dollar or inflation or interest or stock_market or crypto):
        query: object = Query()
        data: dict = query.report_data_query(q_dollar=dollar, q_inflation=inflation,
                                             q_interest=interest, q_stock_market=stock_market,
                                             q_crypto=crypto)

        pdf_data = generate_pdf(data, q_dollar=dollar, q_inflation=inflation,
                                q_interest=interest, q_stock_market=stock_market,
                                q_crypto=crypto)

        pdf_stream = BytesIO(pdf_data)

        response = StreamingResponse(pdf_stream, media_type="application/pdf", headers={
            "Content-Disposition": "attachment; filename=ReporteWorthIt.pdf"})

        redirect = RedirectResponse(url="/")

        response.headers["on_complete"] = redirect.headers["location"]
    else:
        response = RedirectResponse(url="/")

    return response
