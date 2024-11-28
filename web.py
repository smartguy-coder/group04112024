from pywebio.input import input as pw_input
from pywebio.output import put_text

import money
import phrases
import constants



put_text(phrases.MSG_WELCOME.format(rest=constants.restaurant_name))
