my_dict = {
    'name': 'Dagmawi',
    'batch': 3,
    'department': 'Mechatronics'
}

batch_value = my_dict.pop('batch')
print(f"Removed batch: {batch_value}")
print(my_dict)

try:
    my_dict.pop('university')
except KeyError as e:
    print(f"Error: {e}")

university_value = my_dict.pop('university', 'AASTU')
print(f"Country value: {university_value}")
print(my_dict)