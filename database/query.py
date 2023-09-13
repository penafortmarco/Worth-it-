from .connection import DataBase
from config.gcv import BITCOIN_COIN_NAME, ETHEREUM_COIN_NAME, DAI_COIN_NAME


class Query(DataBase):

    def __init__(self):
        super().__init__()

    def data_query(self) -> dict:
        response: dict = dict(self.collection.find_one({}))
        self.client.close()
        return response

    def report_data_query(self, q_dollar: bool = False, q_inflation: bool = False,
                          q_interest: bool = False, q_stock_market: bool = False,
                          q_crypto: bool = False) -> dict:

        response: dict = self.data_query()
        elements_in_report: list = []

        elements_in_report.extend(check_statics_elements(
            q_dollar, q_inflation, q_interest))

        elements_in_report.extend(
            check_dynamics_elements(q_stock_market, q_crypto))

        total_keys: list = response.copy().keys()

        for key in total_keys:
            if key not in elements_in_report:
                del response[key]

        return response

    def update_data(self, data: dict):
        self.collection.update_one({}, {'$set': data})
        self.client.close()


def check_statics_elements(dollar: bool, inflation: bool, interest: bool) -> dict:

    elements_in_report: list = []
    if dollar:
        keys_in_dollar: list = ['official_dollar',
                                'blue_dollar',
                                'difference_dollar']
        elements_in_report.extend(keys_in_dollar)

    if inflation:
        keys_in_inflation: list = ['annual_inflation',
                                   'accumulated_inflation',
                                   'current_inflation']
        elements_in_report.extend(keys_in_inflation)

    if interest:
        keys_in_interest: list = ['min_interest_rate',
                                  'max_interest_rate',
                                  'average_interest_rate']
        elements_in_report.extend(keys_in_interest)

    return elements_in_report


def check_dynamics_elements(stock_market: bool, crypto: bool) -> dict:

    elements_in_report: list = []

    if stock_market:
        keys_in_stock_market: list = ['average_stockmarket_variation',
                                      'max_stockmarket_rise',
                                      'min_stockmarket_rise']
        elements_in_report.extend(keys_in_stock_market)

    if crypto:
        keys_in_crypto: list = [f'{BITCOIN_COIN_NAME}_price',
                                f'{BITCOIN_COIN_NAME}_variation_percentage',
                                f'{ETHEREUM_COIN_NAME}_price',
                                f'{ETHEREUM_COIN_NAME}_variation_percentage',
                                f'{DAI_COIN_NAME}_price',
                                f'{DAI_COIN_NAME}_variation_percentage']
        elements_in_report.extend(keys_in_crypto)

    return elements_in_report
