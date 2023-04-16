from data import Data
from gcv import DOLLAR_SCRAP_URL


class Dollar(Data):

    def __init__(self, target_page=DOLLAR_SCRAP_URL):
        super().__init__(target_page)

    def _extract_data(self, soup):
        """Override from Class Data. It recibes a BeatifoulSoup object. Find all necessary values by id. Finally
        returns all exctracted values in a tuple."""

        official_dollar_purchase_price = soup.find(id='c1').text
        official_dollar_sales_price = soup.find(id='v1').text
        blue_dollar_purchase_price = soup.find(id='c2').text
        blue_dollar_sales_price = soup.find(id='v2').text

        extracted_data = (official_dollar_purchase_price, official_dollar_sales_price,
                          blue_dollar_purchase_price, blue_dollar_sales_price)

        return extracted_data

    def _clean_data(self, data):
        """Override from Class Data. It recibes a tuple of strings. For element in tuple, clean all unwanted characters. 
        Finally returns a list o floats"""

        cleaned_data = []
        for element in data:
            element = element.strip()
            element = element.replace('$', '')
            element = element.replace(',', '.')
            cleaned_data.append(float(element))

        return tuple(cleaned_data)

    def _transform_data(self, data):
        """Override from Class Data. It recibes a tuple of floats. Calculates the average for dollar and the difference 
        between them. Finally a dictionary with all converted values."""

        official_dollar = (data[0] + data[1])/2
        blue_dollar = (data[2] + data[3])/2
        difference_dollar = blue_dollar - official_dollar
        data = {
            'official_dolar': official_dollar,
            'blue_dollar': blue_dollar,
            'difference_dollar': difference_dollar
        }

        return data
