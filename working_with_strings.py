import messages

firstname = "Alex"
print(id(firstname))
lastname = "Obama"

firstname = "Mr " + firstname
print(id(firstname))
fullname = firstname + " " + lastname
welcome_message = "Welcome, Mr." + " " + fullname

alternative_welcome_message = f'Welcome, Mr. {fullname}!'
print(alternative_welcome_message)
alternative_welcome_message2 = messages.MSG_WELCOME_MISTER.format(name='George', other='Other data')
print(alternative_welcome_message2)

print(welcome_message)

reverted_fullname = lastname + firstname

print(fullname)
print(reverted_fullname)

print(firstname, lastname, lastname, fullname)

#
# multy_lines1 = ('m,hhhhhhhjk h dkfghkdgl df gdfhg ggggdfjkdfh kjdfh jkdfhg jkfdhgkjlfdh grtuy rt ioturtioptuyiop toiptu '
#                 'ypturytfuhgopirtrtyirty rt urtuy ytu'
#                 'dlfkhgjkldfhgjklfdhjgkdfgkjg'
#                 'dlfkhgjkldfhgjklfdhjgkdfgkjg'
#                 'dlfkhgjkldfhgjklfdhjgkdfgkjg'
#                 'dlfkhgjkldfhgjklfdhjgkdfgkjg'
#                 )
# print(multy_lines1)
#
# multy_lines2 = 'm,hhhhhhhjk h dkfghkdgl df\n\n gdfhg ggggdfjkdfh kjdfh \njkdfhg jkfdhgkjlfdh grtuy rt ioturtioptuyiop toiptu '
#
# print(multy_lines2)


multy_lines3 = """
rtgrd
gdfg
dfg
dfg
df
gdf
gfdgdfg

"""

print(multy_lines3)

my_text = 'my best text'

pass
