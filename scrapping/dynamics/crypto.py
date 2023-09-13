from scrapping.data_models.dynamic_data import DynamicData
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from config.gcv import CRYPTO_SCRAP_URL


class Crypto(DynamicData):

    def __init__(self, coin: str, target_page: str = CRYPTO_SCRAP_URL):
        target_page = target_page + coin
        self.coin_name = coin
        super().__init__(target_page)

    def _extract_data(self, driver: object) -> tuple:
        """ Extracts data from a web page using a WebDriver object and returns it as a tuple.
        It receives a WebDriver object for interacting with the web page. Then look for the values 
        using BeatifoulSoup and returns them in a tuple."""

        html_target_element: object = driver.find_element(
            By.ID, 'crypto__variation')

        html_target_element: str = html_target_element.get_attribute(
            'outerHTML')

        soup: object = BeautifulSoup(html_target_element, 'html.parser')
        buy: object = soup.find(class_='--buy')
        buy_price: str = buy.find(class_='--price').text.strip()

        sell: object = soup.find(class_='--sell')
        sell_price: str = sell.find(class_='--price').text.strip()

        variation: object = soup.find(class_='--variation')
        variation = variation.find(class_='--variation')
        variation_percentage: str = variation.find(
            class_='--price').text.strip()

        extracted_data: tuple = (buy_price, sell_price, variation_percentage)

        return extracted_data

    def _clean_data(self, data: tuple) -> tuple:

        cleaned_data: list = []

        for element in data:
            cleaned_element: float = float(
                element.replace(',', '.').replace('$', ''))
            cleaned_data.append(cleaned_element)

        return tuple(cleaned_data)

    def _transform_data(self, data: tuple) -> dict:

        crypto_price: float = round((data[0] + data[1]) / 2, 2)
        variation_percentage: float = data[2]

        data: dict = {
            f'{self.coin_name}_price': crypto_price,
            f'{self.coin_name}_variation_percentage': variation_percentage
        }

        return data
