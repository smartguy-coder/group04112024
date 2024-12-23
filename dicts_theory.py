# login = 'admin'
# password = '123'
box = {}
list_ = []
string_ = ''

admin_data = {
    'login': 'admin658',
    'password': '123',
    'name': 'Андрій',
    'age': 40,
    'hobbies': ['soccer', 'chess'],
    'address': {
        'city': 'Одеса',
        'post_code': 65088,
        'flat': None,
    }
}

admin_login = admin_data['login']
admin_age = admin_data['age']
admin_first_hobby = admin_data['hobbies'][0]
admin_city = admin_data['address']['city']
admin_street = admin_data['address'].get('street')
admin_flat = admin_data['address'].get('flat')
admin_flat2 = admin_data['address']['flat']

admin_data['surname'] = "Дорошенко"
admin_surname = admin_data['surname']

admin_data['address']['street'] = 'Садова'
admin_data['hobbies'].append('swimming')
admin_data['age'] = 41

pass











