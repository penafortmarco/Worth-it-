from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config. gcv import MONGODB_REMOTE_USER, MONGODB_REMOTE_PASSOWORD


class DataBase():

    def __init__(self):
        uri: str = f'mongodb+srv://{MONGODB_REMOTE_USER}:{MONGODB_REMOTE_PASSOWORD}@worthit.eccx8my.mongodb.net/?retryWrites=true&w=majority'
        try:
            self.client = MongoClient(uri, server_api=ServerApi('1'))
            self.db = self.client.WorthIt
            self.collection = self.db.data
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
