from data import Data
from gcv import INFLATION_SCRAP_URL


class Inflation(Data):

    def __init__(self, target_page=INFLATION_SCRAP_URL):
        super().__init__(target_page)

    def _extract_data(self, soup):
        """Override from Class Data. It recibes a BeatifoulSoup object. The target data is located in the first row 
        of the table. So, extracts all the table the find() method and then uses find_all() to take all columns in a 
        list. Finally returns a list of HTML divs."""

        table = soup.find('tbody')
        row = table.find('tr')
        extracted_data = row.find_all(class_='numero')

        return extracted_data

    def _clean_data(self, data):
        """Override from Class Data. It recibes a list of divs. All wanted values are in the HTML attr 'data-value'. 
        Uses a list comprehension to get all values from divs and convert them to float. Finally returns a list of floats"""

        cleaned_data = [float(div.get('data-value')) for div in data]

        return cleaned_data

    def _transform_data(self, data):
        """Override from Class Data. It recibes a list of floats. It take all values by index. Finally returns a dictionary
        with all converted values."""

        annual_inflation = data[0]
        accumulated_inflation = data[1]
        current_inflation = data[2]

        data = {
            'annual_inflation': annual_inflation,
            'accumulated_inflation': accumulated_inflation,
            'current_inflation': current_inflation
        }

        return data
