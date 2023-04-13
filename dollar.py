from data import Data
from gcv import DOLLAR_SCRAP_URL

class Dollar(Data):

    def __init__(self, target_page = DOLLAR_SCRAP_URL):
        super().__init__(target_page)

    def _extract_data(self, data):
        """Override from Class Data. It recibes a BeatifoulSoup object. Find all necessary values by id. Then
        return all exctracted values in a tuple."""

        official_dollar_purchase_price = data.find(id='c1').text
        official_dollar_sales_price = data.find(id='v1').text
        blue_dollar_purchase_price = data.find(id='c2').text
        blue_dollar_sales_price = data.find(id='v2').text

        return (official_dollar_purchase_price, official_dollar_sales_price,
                blue_dollar_purchase_price, blue_dollar_sales_price)

    def _clean_data(self, data):
        """Override from Class Data. It recibes a BeatifoulSoup object. For element in BeatifoulSoup object, clean all
        unwanted characters. Then returns all wanted values in a tuple."""

        cleaned_data = []
        for element in data:
            element = element.strip()
            element = element.replace('$', '')
            element = element.replace(',', '.')
            element = float(element)
            cleaned_data.append(element)

        return tuple(cleaned_data)

    def _transform_data(self, data):
        """Override from Class Data. It recibes a BeatifoulSoup object. Calculates the average for dollar and the difference
        between them. Then return a dictionary wiith that values."""

        official_dollar = (data[0] + data[1])/2
        blue_dollar = (data[2] + data[3])/2
        difference = blue_dollar - official_dollar
        values = {
            'dolar_oficial': official_dollar,
            'dolar_blue': blue_dollar,
            'dolar_brecha': difference
        }
        return values
