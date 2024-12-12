import functions

marks_in_school = [
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [12, 12, 10, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [1, 6, 7, 10],
]

for student_marks in marks_in_school:
    functions.send_unhappy_sms(student_marks=student_marks)
    functions.send_bad_marks_to_parents(marks=student_marks)
