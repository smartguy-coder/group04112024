# file = open('data.txt', mode='r')
# data = file.read()
# print(data)
# file.close()


# with (
#     open('data.txt', mode='w', encoding='utf-8') as file,
#     open('main.py', mode='r', encoding='utf-8') as file2,
#     open('money.py', mode='a') as file3
# ):
#     data2 = file2.read()
#     print(data2)
#
#     file.write(data2)
#
#     file3.write('print(5555)\n')

# CSV
# 1
# with open('students.csv', mode='r', encoding='utf-8') as file:
#     # data = file.read()
#     srudents_data = file.readlines()
#     students = []
#     for row, student in enumerate(srudents_data, start=1):
#         if row == 1:
#             continue
#         student_clean = student.strip().split(',')
#         student_name = student_clean[1]
#         students.append(student_name)
#         pass

# with open('a', mode='a', encoding='utf-8') as file:
#     file.write('10,,Sony\n')

# 2
import csv

# with open('students.csv', mode='r', encoding='utf-8') as file:
#     reader = csv.reader(file, delimiter=',')
#     for row in reader:
#         print(row)

# with open('students.csv', mode='r', encoding='utf-8') as file2:
#     reader = csv.DictReader(file2, delimiter=',')
#     for row in reader:
#         print(row)
#
with open('students.csv', mode='a', newline='') as file3:
    fieldnames = ['number', 'name', 'surname']
    data = [
        {'number': '13', 'name': 'John', 'surname': 'Schmidt'},
        {'number': '144', 'name': 'John', 'surname': 'Other'},
    ]
    writer = csv.DictWriter(file3, fieldnames=fieldnames)
    writer.writerows(data)

