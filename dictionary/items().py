my_dict = {
    'name': 'Dagmawi',
    'batch': 3,
    'department': 'Mechatronics'
}
items = my_dict.items()
print(items)

for key, value in my_dict.items():
 print(f"{key}: {value}")

my_dict['university'] = 'AASTU'
print(my_dict.items())