from pymongo import MongoClient
from decouple import config

class MongoInfrastructure:

    client = None
    uri = config('uri')
    db_name = config('db_name')
    db_collection = config('db_collection')

    @classmethod
    def get_client(cls):
        if cls.client is None:
            cls.client = MongoClient(cls.uri)
        return cls.client
    @classmethod
    def get_db_and_collection(cls):
        client = cls.get_client()
        database = client[cls.db_name]
        collect = database[cls.db_collection]
        return collect
