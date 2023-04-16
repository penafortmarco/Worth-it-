from data import Data
from gcv import INTEREST_RATE_SCRAP_URL


class Interest(Data):

    def __init__(self, target_page=INTEREST_RATE_SCRAP_URL):
        super().__init__(target_page)

    def _extract_data(self, soup):
        """Override from Class Data. It recibes a BeatifoulSoup object. Find a necessary table by class. Then uses a
        list comprehension to take the third column of all rows (where is the target data). Finally returns a list of 
        HTML divs."""

        table = soup.find(
            class_='table table-BCRA table-bordered table-hover table-responsive')

        extracted_data = [row.find_all(
            'td')[2].text for row in table.find_all('tr') if row.find_all('td')]

        return (extracted_data)

    def _clean_data(self, data):
        """Override from Class Data. It recibes a list of divs. Set 'unwanted_chars' with all values that are not usefull. 
        For element in list, clean all unwanted characters. Finally returns a list of floats"""

        unwanted_chars = 'rnt'
        cleaned_data = []
        for element in data:
            element = element.replace(unwanted_chars, '').replace(
                '%', '').replace(',', '.')
            element = element.strip()
            cleaned_data.append(float(element))

        return cleaned_data

    def _transform_data(self, data):
        """Override from Class Data. It recibes a list of floats. Set min and max values of the list. Calculates the average
        of the list. Finally returns a dictionary with all converted values."""

        min_interest_rate = min(data)
        max_interest_rate = max(data)
        average_interest_rate = round((sum(data) / len(data)), 2)

        data = {
            'min_interest_rate':  min_interest_rate,
            'max_interest_rate': max_interest_rate,
            'average_interest_rate': average_interest_rate
        }

        return data
