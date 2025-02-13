from config import uri

from pymongo.mongo_client import MongoClient

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
wanted_book = collection_books.find_one({'author': 'Т.Г. Шевченко', 'price': 130})
print(wanted_book)
