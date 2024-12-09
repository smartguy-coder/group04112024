import logging

from pywebio.input import input as pw_input, slider, checkbox, radio
from pywebio.input import PASSWORD as PW_PASSWORD, NUMBER, FLOAT
from pywebio.input import textarea
from pywebio.output import put_text, put_error, put_success, put_warning, put_html

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

LOGIN = '1'
PASSWORD = '1'

# HEADER
put_html('<h1>Welcome to the name processor</h1>')
put_html('<h2>demo version</h2>')

# GET LOGGING DATA
login = pw_input(label='Enter your login', required=True)
logging.info(f'User entered login {login}')

password = pw_input(label='Enter your password', required=True, type=PW_PASSWORD)
logging.debug(f'User entered password {password}')

is_correct_login = LOGIN == login  # True or False
logging.debug(f'User correct login: {is_correct_login}')
is_correct_password = PASSWORD == password  # True or False
# is_correct_password = True
# is_correct_password = False

# PROCESS LOGIN
if is_correct_login and is_correct_password:
    put_success('You are logged in')

    # PROCESS GIVEN NAME
    # given_name = textarea(label='Enter your name', required=True, placeholder='Enter your data here', minlength=3,
    #                       maxlength=500)

    given_name = pw_input(label='Enter your name and surname', required=True).strip().title()

    given_name_parse = given_name.split()
    name = given_name_parse[0]
    surname = given_name_parse[1]
    put_success(f'yor name {name}')
    put_success(f'yor surname {surname}')


    if given_name == LOGIN:
        put_warning('Your login is similar to your name')

    name_length = len(given_name)
    if name_length == 1:
        put_success(f'Strange name with length {name_length}')
    elif name_length > 50:
        put_success(f'your name contains more 50 symbols {name_length}')
    elif name_length > 20:
        put_success(f'your name contains more 20 symbols {name_length}')
    elif 10 <= name_length <= 15:
        #     elif name_length >= 10 and name_length <= 15    ==========>>>>>>>>>> 10 <= name_length <= 15
        put_success(f'your name contains 10-15 symbols {name_length}')
    elif name_length < 5:
        put_success(f'your name contains less than 5 symbols {name_length}')
    else:
        put_success(f'Name with length {name_length}')

    weight = pw_input(label='Enter your weight', required=True, type=NUMBER, min=25, max=150, value=50)
    weight2 = slider(label='Enter your weight in slider', required=True, type=FLOAT, min=25, max=150, value=50)

    hobbies = ['tennis', 'soccer', 'chess']
    favorite_hobbies = checkbox(label='Choose your favorite hobbies', options=hobbies)
    put_text(favorite_hobbies)

    grades = [5, 6, 9, 11, 'other']
    user_grade = radio(label='Your grade', options=grades)
    put_text(user_grade)

    logging.debug(f'given name: {name}')
else:
    # is_correct_login and is_correct_password:
    # True                   False
    # False                  True
    # False                  False
    put_text('Incorrect login or password')

put_error('The end')
