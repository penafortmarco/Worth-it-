from abc import ABC, abstractmethod


class Data(ABC):

    @abstractmethod
    def __init__(self, target_page: str):
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

    def _final_data(self, source: object) -> dict:
        """Executes all functions and returns the final processed data"""

        data = self._extract_data(source)
        data = self._clean_data(data)
        data = self._transform_data(data)
        return data
    pass
