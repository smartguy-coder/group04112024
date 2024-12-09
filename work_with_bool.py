import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

data1 = 56565
data2 = 0.00
text1 = 'kjdfbhjkdf'
text2 = ' '
text3 = ''
logging.debug(f'{bool(data1)=}')
logging.debug(f'{bool(data2)=}')
logging.debug(f'{bool(text1)=}')
logging.debug(f'{bool(text2)=}')
logging.debug(f'{bool(text3)=}')

# print(True + False + True + 3)
string_length1 = len(text1)
string_length2 = len(text2)
string_length3 = len(text3)

if text1 == text2 and data1 and True:
    pass
pass
