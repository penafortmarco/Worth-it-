from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


def generate_pdf(data: dict, q_dollar: bool = False,
                 q_inflation: bool = False, q_interest: bool = False,
                 q_stock_market: bool = False, q_crypto: bool = False):

    pdf_values = correct_titles(data, q_dollar, q_inflation,
                                q_interest, q_stock_market, q_crypto)

    pdf = draw_pdf(pdf_values)
    return pdf


def correct_titles(data, dollar: bool = False,
                   inflation: bool = False, interest: bool = False,
                   stock_market: bool = False, crypto: bool = False):

    dollar_titles: dict = {}
    inflation_titles: dict = {}
    interest_titles: dict = {}
    stock_market_titles: dict = {}
    crypto_titles: dict = {}

    if dollar:
        dollar_titles = {'Dólar': '',
                         'Oficial': data['official_dollar'],
                         'Blue': data['blue_dollar'],
                         'Diferencia': data['difference_dollar']}
    if inflation:
        inflation_titles = {'Inflación': '',
                            'Anual': f"{data['annual_inflation']}%",
                            'Acumulada': f"{data['accumulated_inflation']}%",
                            'Actual': f"{data['current_inflation']}%"}
    if interest:
        interest_titles = {'Tasa de interés': '',
                           'Mínimo interés': f"{data['min_interest_rate']}%",
                           'Máximo interés': f"{data['max_interest_rate']}%",
                           'Promedio de interés': f"{data['average_interest_rate']}%"}
    if stock_market:
        stock_market_titles = {'Variantes de la bolsa': '',
                               'Promedio de variación': f"{data['average_stockmarket_variation']}%",
                               f"Máxima  ({data['max_stockmarket_rise'][0]})": f"{data['max_stockmarket_rise'][1]}%",
                               f"Mínima ({data['min_stockmarket_rise'][0]})": f"{data['min_stockmarket_rise'][1]}$"}
    if crypto:
        crypto_titles = {'Criptomonedas': '',
                         f"BTC (Variación {data['bitcoin_variation_percentage']}%)": data['bitcoin_price'],
                         f"ETH (Variación {data['ethereum_variation_percentage']}%)": data['ethereum_price'],
                         f"DAI (Variación {data['dai_variation_percentage']}%)": data['dai_price']}

    final_titles = {**dollar_titles,
                    **inflation_titles,
                    **interest_titles,
                    **stock_market_titles,
                    **crypto_titles}

    return final_titles


def draw_pdf(data):

    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    normal_style = styles["Normal"]

    sub_title_style = ParagraphStyle(
        name="subTitle", parent=title_style, fontSize=16, textColor=colors.red)
    main_title_style = ParagraphStyle(
        name="MainTitle", parent=title_style, fontSize=20, textColor=colors.blue)

    margin = 50
    page_width, page_height = letter

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=(page_width, page_height),
                            leftMargin=margin, rightMargin=margin, topMargin=margin, bottomMargin=margin)
    elements = []

    main_title = Paragraph("<u><b>Reporte Worth It</b></u>", main_title_style)
    elements.append(main_title)
    elements.append(Spacer(1, 20))

    for key, value in data.items():
        if value == "":
            paragraph = Paragraph(f"<u><b>{key}</b></u>", sub_title_style)
            elements.append(paragraph)
            elements.append(Spacer(1, 20))
        else:
            paragraph = Paragraph(f"<b>{key}:</b> {value}", normal_style)
            elements.append(paragraph)
            elements.append(Spacer(1, 10))

    doc.build(elements)
    buffer.seek(0)
    return buffer.getvalue()
