from pprint import pprint

from config import uri

from pymongo.mongo_client import MongoClient
from bson import ObjectId

client = MongoClient(uri)

db = client.shop

collection_books = db.books
collection_phones = db.phones

# CREATE
# add one document
# book = {'title': '10 negro', 'price': 365, 'year': 2022, 'content': "Роман вперше був виданий в Лондоні під назвою «Десятеро негренят» (англ. Ten little niggers). В американському виданні наступного 1940 року книга вийшла під назвою «І не лишилось жодного», подальші американські перевидання використовували цю назву, хоча у період між 1964 і 1986 роками у США роман виходив під назвою «Десятеро маленьких індіанців» (англ. Ten little Indians). Британські видання продовжували використовувати оригінальну назву до 1985 року[3]. З 2000-х років у багатьох країнах на тлі протестів проти расизму почали використовувати нові назви для роману, а також його театральних чи кінематографічних адаптацій.[4][5][6][7][8][9][10][11][12] 2020 року після того як Amazon France вилучила роман з оригінальною назвою зі своєї торгової платформи власник авторських прав на роман правнук Агати Крісті Джеймс Прічард рекомендував не видавати роман під назвою «Десятеро негренят» не лише у Франції, а й по всьому світу"}
# collection_books.insert_one(book)

# add many
# books = [
#     {'title': 'I, legend', 'price': 500.36, 'year': 1976, 'metadata': {'anotherField': 55}},
#     {'title': 'Кобзар', 'author': "Т.Г. Шевченко", 'price': 100},
#     {'title': 'Кобзар', 'author': "Т.Г. Шевченко", 'price': 111},
#     {'title': 'Кобзар', 'author': "Т.Г. Шевченко", 'price': 112},
#     {'title': 'Кобзар', 'author': "Т.Г. Шевченко", 'price': 130},
# ]
# collection_books.insert_many(books)


# READ
# first
# first_book = collection_books.find_one()
# print(first_book)

# one by filter
# wanted_book = collection_books.find_one({'author': 'Т.Г. Шевченко', 'price': 130})
# print(wanted_book)

# find many
# books = collection_books.find()
# # result = list(result)
# # pprint(result)
# for book in books:
#     pprint(book)
# print(55555555555555555)
# for book in books:
#     pprint(book)

# query = {'author': 'Т.Г. Шевченко'}
# query = {'price': 250}
# query = {'price': {'$gt': 300}}
# query = {'price': {'$gt': 300, '$lt': 500}}
# query = {'price': {'$gte': 499, '$lte': 500.36}}
# query = {
#     'price': {'$gte': 499, '$lte': 500.36},
#     'author': 'Т.Г. Шевченко',
# }
# query = {
#     'title': {'$regex': 'I,*'},  # * -> any sequence of letters
# }

# query = {
#     'content': {
#         '$regex': 'десятеро',
#         '$options': 'i',  # if i -> any register
#     },
# }
# query = {
#     'content': {
#         '$regex': '^впер', # ^ -> field starts with expression
#         '$options': 'i',  # if i -> any register
#     },
# }
# query = {
#     'content': {
#         '$regex': '^в..рше ',  # . -> any single letter
#         '$options': 'i',  # if i -> any register
#     },
# }

# query = {
#     'content': {
#         '$regex': 'сві.у$',  # $ -> field ends with expression
#         '$options': 'i',  # if i -> any register
#     },
# }
# query = {
#     'content': {
#         '$not': {'$regex': 'сві.у$'}
#     }
# }
# query = {}
# query = {}
#
# books = collection_books.find(query).limit(5).sort('price', -1).skip(2)
# for book in books:
#     pprint(book)

# number = int('10', 10)
# print(number)
# number = int('67ae429ea0c78ed781e21d9e', 16)  # 32087623706570306220426665374
# print(number)
# query = {'_id': ObjectId('67ae429ea0c78ed781e21d9e')}
#
# defined_book = collection_books.find_one(query)
# pprint(defined_book)


# UPDATE
# use $set
# query = {'price': 500.36}
# new_data = {'$set': {'price': 510}}
# updated = collection_books.update_one(query, new_data)
# print(updated)

# query = {'price': 510}
# new_data = {'$set': {'price': 1200, 'newData': True}}
# updated = collection_books.update_many(query, new_data)
# print(updated)

# multiplication
# query = {}
# new_data = {'$mul': {'price': 0.5}}
# updated = collection_books.update_many(query, new_data)
# print(updated)

# increase
# query = {}
# new_data = {'$inc': {'price': -15}}
# updated = collection_books.update_many(query, new_data)
# print(updated)

# together
# query = {}
# new_data = {'$inc': {'warranty': 10, 'cost': 3.5}, '$mul': {'price': 1.25}, '$set': {'brand': 'a-ba-ba-la-ma-ga'}}
# updated = collection_books.update_many(query, new_data)
# print(updated)

#  DELETE field
# query = {'_id': ObjectId('67ae429ea0c78ed781e21d9e')}
# operation = {'$unset': {'warranty': 1}}
# updated = collection_books.update_many(query, operation)
# print(updated)

#  DELETE document
# query = {'_id': ObjectId('67ae429ea0c78ed781e21d9e')}
# updated = collection_books.delete_many(query)
# print(updated)

collection_books.drop()
client.drop_database(db)

