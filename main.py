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

# book1 = {"title": 'History', 'price': 325}
# books_collection.insert_one(book1)
#
# ## many
# mops = [
#     {'price': 125, "series": 'FFFD'},
#     {'price': 656, "series": 'gfdgfdg'},
#     {'price': 5552, "series": 'dfg'},
# ]
# mops_collection.insert_many(mops)

# READ
# first

# result = books_collection.find_one()
# print(result)

# query = {"price": 325}
# result = books_collection.find_one(query)
# print(result)

# query = {"price": 325, "title": 'History'}
# result = books_collection.find_one(query)
# print(result)

# find many

# result = books_collection.find()
# print(result)
# for r in result:
#     if r['title'] == 'History':
#         print(r)
#         break
#     print(r)
#
# print(111111111111111111)
#
# for r in result:
#     print(r)

# query = {"price": 325}
# query = {"price": {'$gt': 500}}
# query = {"price": {'$gte': 500}}
# query = {"price": {'$gte': 500, '$lte': 2000}}
# query = {
#     "price": {'$gte': 500, '$lte': 2000},
#     'title': {"$regex": 'Ukr*', '$options': 'i'}
# }
# # result = books_collection.find(query)
# result = books_collection.find(query).limit(10).sort('price', -1).skip(1)
#
# for r in result:
#     print(r)

# UPDATE

# use $set
query = {}
# query = {"price": 325}
new_data = {'$set': {'tag': 'best choice', 'price': 327}}
# update_result = books_collection.update_one(query, new_data)
# print(update_result)
result = books_collection.update_many(query, new_data)
print(result.raw_result)

# use multiplication
# query = {}
# operation = {'$mul': {'price': 0.5}}
# update_result = books_collection.update_many(query, operation)
# print(update_result.raw_result)

# use increase
# query = {}
# operation = {'$inc': {'price': -25}}
# update_result = books_collection.update_many(query, operation)
# print(update_result.raw_result)


# DELETE
## delete fields
# query = {}
# operations = {'$unset': {'tag': 1}}
# result = books_collection.update_many(query, operations)
# print(result.raw_result)

## delete document
# query = {'price': -13}
# result = books_collection.delete_many(query)
# print(result.raw_result)

#delete collection

# mops_collection.drop()
# client.drop_database(database)
