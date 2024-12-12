from constants_marks import MIN_SUCCESS_MARK, MIN_PARENTS_SATISFY
# from functions import send_unhappy_sms
import functions

my_marks = [9, 10, 6, 12, 5]

is_contain_6 = 6 in my_marks
is_not_contain_5 = 5 not in my_marks

is_contain_a = 'a' in 'data алорполапл варлоп  '
is_contain_a_in_list = 'a' in my_marks
is_contain_b = 'b' in 'data'
is_contain_da = 'da' in 'data'
message = 'Я відвідав на вихідних Одесу, Харків та Київ - ох і тиждень був. Одеса була дощливою!!!'
is_odesa_visited = 'одес' in message.lower()

if is_odesa_visited:
    print('Send SMS: Dude, pay your debt!!!')

functions.send_unhappy_sms(student_marks=my_marks)
functions.send_unhappy_sms(student_marks=[11, 2])

functions.send_bad_marks_to_parents(student_marks=my_marks)




