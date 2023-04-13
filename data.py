from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests


class Data(ABC):

    def __init__(self, target_page):
        try:
            response = requests.get(target_page)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                data = self._final_data(soup)
                self.data = data
            else:
                raise ValueError(f'Error: {response.status_code}')
        except ValueError as ve:
            print(ve)
        
    @abstractmethod
    def _extract_data(self):
        pass

    @abstractmethod
    def _clean_data(self):
        pass
    
    @abstractmethod
    def _transform_data(self):
        pass 

    def _final_data(self, soup):
        data = self._extract_data(soup)
        data = self._clean_data(data)
        data = self._transform_data(data)
        return data

    pass

