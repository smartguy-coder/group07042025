from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import config

uri = f"mongodb+srv://{config.MONGO_USER}:{config.MONGO_PASSWORD}@cluster0.pi65akv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


client = MongoClient(uri, server_api=ServerApi('1'))

database = client["warehouse"]
books_collection = database["books"]

book1 = {"title": 'History of Brasil', 'price': 250, 'count': 15, 'tag': 'history'}
books_collection.insert_one(book1)

# 1 stage - $match
query = [
    {'$match': {}}
]

# temp_result = books_collection.aggregate(query)
# print(list(temp_result))

# 2 stage - $group
query = [
    {'$group': {'_id': '$tag'}}
]
# temp_result = books_collection.aggregate(query)
# print(list(temp_result))

# 3 stage $sum

query = [
    {'$group': {'_id': '$tag', 'total_count': {'$sum': '$count'}}}
]
# temp_result = books_collection.aggregate(query)
# print(list(temp_result))

# 4 stage $project

query = [
    {'$project': {'_id': 0, 'title': 1, 'price': 1, 'description': {'$concat': ['$title', ' some description from tag: ', '$tag']}}}
]
# temp_result = books_collection.aggregate(query)
# print(list(temp_result))

# FINAL AGGREGATION
query = [
    {'$match': {'price': {'$gt': 250}}},
    {'$project': {'_id': 0, 'title': 1, 'price': 1, 'count': 1, 'cost': {"$multiply": ['$price', '$count', 1.5]}}},
    {'$match': {'cost': {'$gt': 1000}}},
]

temp_result = books_collection.aggregate(query)
print(list(temp_result))
