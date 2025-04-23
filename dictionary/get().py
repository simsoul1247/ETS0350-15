my_dict = {
    'name': 'Dagmawi',
    'department': 'Mechatronics'
}
name = my_dict.get('name')
print(name)

department = my_dict.get('department')
print(department)

university = my_dict.get('university', 'AASTU')
print(university)

batch = my_dict.get('batch')
print(batch)