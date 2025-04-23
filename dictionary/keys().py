my_dict = {
    'name': 'Dagmawi',
    'batch': 3,
    'department': 'Mechatronics'
}

keys = my_dict.keys()
print(keys)

for key in my_dict.keys():
    print(f"Key: {key}")

my_dict['university'] = 'AASTU'
print(my_dict.keys())