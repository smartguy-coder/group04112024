import logging

from pywebio.input import input as pw_input
from pywebio.input import PASSWORD as PW_PASSWORD
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
is_correct_password = PASSWORD == password    # True or False
# is_correct_password = True
# is_correct_password = False

# PROCESS LOGIN
if is_correct_login and is_correct_password:
    put_success('You are logged in')

    # PROCESS GIVEN NAME
    # given_name = textarea(label='Enter your name', required=True, placeholder='Enter your data here', minlength=3,
    #                       maxlength=500)

    given_name = pw_input(label='Enter your name', required=True).strip()

    if given_name == LOGIN:
        put_warning('Your login is similar to your name')

    name_length = len(given_name)
    if name_length == 1:
        put_success(f'Strange name with length {name_length}')
    else:
        put_success(f'Name with length {name_length}')







    logging.debug(f'given name: {given_name}')
else:
    # is_correct_login and is_correct_password:
    # True                   False
    # False                  True
    # False                  False
    put_text('Incorrect login or password')





put_error('The end')
