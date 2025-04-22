keys = ['name', 'age', 'hobbies']
default_dict = dict.fromkeys(keys)
print("Dictionary with default values:", default_dict)

value_dict = dict.fromkeys(keys, 'unknown')
print("Dictionary with specified values:", value_dict)

mutable_value_dict = dict.fromkeys(keys, [])
print("Dictionary with mutable default value:", mutable_value_dict)

mutable_value_dict['hobbies'].append('reading')
print("Modified mutable value dictionary:", mutable_value_dict)