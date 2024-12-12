given_name = 'vasyl Kartychak'  # input()
given_name = given_name.title()
analizing_data = given_name.split()


# s1 = '11111'
# print(id(s1))
#
# s1 = s1 + '2'
# print(id(s1))


students = ['Vasyl', 'Anna', 'Alex']


pencils = ['grey', 'black']
crayons = ['red', 'black', 'black', 'blue']
print(id(crayons))
pencil_red = crayons[0]
pencil_red_2 = crayons[-4]

# sort list
crayons.sort(reverse=True)

# add element
crayons.append('orange')
print(id(crayons))

# merge 2 lists
# crayons.append(pencils)
crayons.extend(pencils)

# remove element
crayons.remove('black')
print(id(crayons))

crayons.pop()  # last el
crayons.pop(0)  # by index


# what_is_list = ['Vasyl', 'Kartychak', 55, [559], True, False, 3.96]
print(students)
pass

my_list = [9, 10, 6, 12]
my_list.append(7)

my_list.insert(255, 11)
my_list[3] = 8
