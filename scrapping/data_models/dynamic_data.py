from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.common.by import By
from scrapping.data_models.data import Data


class DynamicData(Data, ABC):

    def __init__(self, target_page: str):

        try:
            driver = webdriver.Chrome()
            driver.get(target_page)
            driver.implicitly_wait(3)
            self.data: dict = self._final_data(driver)
        except TypeError as e:
            pass

    @abstractmethod
    def _extract_data(self):
        pass

    @abstractmethod
    def _clean_data(self):
        pass

    @abstractmethod
    def _transform_data(self):
        pass
