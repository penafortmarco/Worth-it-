from scrapping.dynamics.stock_market import StockMarket
from scrapping.dynamics.crypto import Crypto
from scrapping.statics.dollar import Dollar
from scrapping.statics.inflation import Inflation
from scrapping.statics.interest import Interest
from database.query import Query
from config.gcv import BITCOIN_COIN_NAME, ETHEREUM_COIN_NAME, DAI_COIN_NAME


class CronJob():
    def __init__(self):
        pass

    def _scrap_data(self):
        dollar: object = Dollar()
        inflation: object = Inflation()
        interest: object = Interest()
        stock_market: object = StockMarket()
        bitcoin: object = Crypto(BITCOIN_COIN_NAME)
        ethereum: object = Crypto(ETHEREUM_COIN_NAME)
        dai: object = Crypto(DAI_COIN_NAME)

        data: dict = {**dollar.data,
                      **inflation.data,
                      **interest.data,
                      **stock_market.data,
                      **bitcoin.data,
                      **ethereum.data,
                      **dai.data}
        return data

    def update_data(self):

        query = Query()
        data = self._scrap_data()
        query.update_data(data)


job = CronJob()
job.update_data()
