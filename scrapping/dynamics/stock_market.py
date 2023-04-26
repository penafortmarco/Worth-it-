from scrapping.data_models.dynamic_data import DynamicData
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from gcv import STOCK_MARKET_SCRAP_URL


class StockMarket(DynamicData):

    def __init__(self, target_page=STOCK_MARKET_SCRAP_URL):
        super().__init__(target_page)

    def _extract_data(self, driver: object) -> tuple:

        html_target_element = driver.find_element(
            By.ID, 'accionesArgCotizacion')

        html_target_element = html_target_element.get_attribute('outerHTML')

        soup: object = BeautifulSoup(html_target_element, 'html.parser')
        table = soup.find('tbody')
        rows = table.find_all('tr')

        extracted_data: tuple = tuple([
            [column.get_text().strip() for column in row.find_all('td')]
            for row in rows
        ])

        return extracted_data

    def _clean_data(self, data: tuple) -> tuple:

        cleaned_data: list = []

        for element in data:
            enterpise: str = element[0]
            variation: float = float(element[3].replace(',', '.'))
            cleaned_data.append([enterpise, variation])

        return tuple(cleaned_data)

    def _transform_data(self, data: tuple) -> dict:

        average_variation: float = 0.0
        max_value: float = 0.0
        min_value: float = 1.0

        for element in data:

            average_variation += element[1]

            if (element[1] > max_value):
                max_value = element[1]
                max_stockmarket_rise = element

            if (element[1] < min_value):
                min_value = element[1]
                min_stockmarket_rise = element

        average_stockmarket_variation: float = round(
            average_variation / len(data), 2)

        data: dict = {
            'average_stockmarket_variation': average_stockmarket_variation,
            'max_stockmarket_rise': max_stockmarket_rise,
            'min_stockmarket_rise': min_stockmarket_rise
        }

        return data
