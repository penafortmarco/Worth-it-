from scrapping.data_models.static_data import StaticData
from config.gcv import INFLATION_SCRAP_URL


class Inflation(StaticData):

    def __init__(self, target_page=INFLATION_SCRAP_URL):
        super().__init__(target_page)

    def _extract_data(self, soup: object) -> tuple:
        """Override from Class Data. It recibes a BeatifoulSoup object. The target data is located in the first row 
        of the table. So, extracts all the table using the find() BeatifoulSoup method and then uses find_all() to take 
        all columns in a list. Finally returns a tuple of HTML divs (str)."""

        table = soup.find('tbody')
        row = table.find('tr')
        extracted_data: tuple = tuple(row.find_all(class_='numero'))

        return extracted_data

    def _clean_data(self, data: tuple) -> tuple:
        """Override from Class Data. It recibes a tuple of divs. All wanted values are in the HTML attr 'data-value'. 
        Uses a list comprehension to get all values from divs and converts them to float. Finally returns a tuple of floats"""

        cleaned_data: tuple = tuple(
            [float(div.get('data-value')) for div in data])

        return cleaned_data

    def _transform_data(self, data: tuple) -> dict:
        """Override from Class Data. It recibes a tuple of floats. It take all values by index. Finally returns a dictionary
        with all converted values."""

        annual_inflation: float = data[0]
        accumulated_inflation: float = data[1]
        current_inflation: float = data[2]

        data: dict = {
            'annual_inflation': annual_inflation,
            'accumulated_inflation': accumulated_inflation,
            'current_inflation': current_inflation
        }

        return data
