from data import Data
from gcv import INFLATION_SCRAP_URL


class Inflation(Data):

    def __init__(self, target_page=INFLATION_SCRAP_URL):
        super().__init__(target_page)

    def _extract_data(self, soup):

        table = soup.find('tbody')
        row = table.find('tr')
        extracted_data = row.find_all(class_='numero')

        return extracted_data

    def _clean_data(self, data):

        cleaned_data = [div.get('data-value') for div in data]
        return cleaned_data

    def _transform_data(self, data):

        data = tuple(map(float, data))

        annual_inflation = data[0]
        monthly_inflation = data[1]
        current_inflation = data[2]

        data = {
            'inflacion_anual': annual_inflation,
            'inflacion_mensual': monthly_inflation,
            'inflacion_actual': current_inflation
        }

        return data
