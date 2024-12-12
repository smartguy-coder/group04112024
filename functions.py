from constants_marks import MIN_SUCCESS_MARK, MIN_PARENTS_SATISFY


def send_unhappy_sms(student_marks):
    for mark in student_marks:
        if mark < MIN_SUCCESS_MARK:
            print(
                f'Send SMS: say something to your child, they got {mark}. Min value for traveling is {MIN_SUCCESS_MARK}')
            break


def send_bad_marks_to_parents(marks):
    bad_marks = []
    for mark in marks:
        if mark < MIN_PARENTS_SATISFY:
            bad_marks.append(mark)
    if bad_marks:
        bad_marks_in_string = ', '.join(map(str, bad_marks))  # from int to str
        #                                     [str(5), str(6)]
        print(f'Send SMS: your child has got next bad marks: {bad_marks_in_string}.')
    else:
        print(f'Send SMS: your child is genius.')
