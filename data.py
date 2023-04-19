from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests


class Data(ABC):
    """Defines an initialization method that makes a request to a target webpage using the requests module. 
    If the request is successful, the HTML content is parsed using BeautifulSoup, and is stored in a data attribute.
    Then, data is cleaned and transformed. 
    If the request fails, a ValueError exception is raised with an error."""

    def __init__(self, target_page: str):

        try:
            response = requests.get(target_page)
            if response.status_code == 200:
                soup: object = BeautifulSoup(response.text, 'html.parser')
                self.data: dict = self._final_data(soup)
            else:
                raise ValueError(f'Error: {response.status_code}')
        except ValueError as ve:
            self.data: dict = {'error_message': ve}

    @abstractmethod
    def _extract_data(self):
        pass

    @abstractmethod
    def _clean_data(self):
        pass

    @abstractmethod
    def _transform_data(self):
        pass

    def _final_data(self, soup: object) -> dict:
        """Executes all functions and returns the final processed data"""

        data = self._extract_data(soup)
        data = self._clean_data(data)
        data = self._transform_data(data)
        return data

    pass
