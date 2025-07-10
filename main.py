from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import config

uri = f"mongodb+srv://{config.MONGO_USER}:{config.MONGO_PASSWORD}@cluster0.pi65akv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


client = MongoClient(uri, server_api=ServerApi('1'))

database = client["warehouse"]
books_collection = database["books"]
mops_collection = database["mops"]

# CREATE
## single

book1 = {"title": '10 negro', 'price': 325}
books_collection.insert_one(book1)

## many
mops = [
    {'price': 125, "series": 'FFFD'},
    {'price': 656, "series": 'gfdgfdg'},
    {'price': 5552, "series": 'dfg'},
]
mops_collection.insert_many(mops)
