my_dict = {
    'a': 1,
    'b': 2
}

value_b = my_dict.setdefault('b', 3)
print("Value of 'b':", value_b)
print("Dictionary after accessing 'b':", my_dict)

value_c = my_dict.setdefault('c', 3)
print("Value of 'c':", value_c)
print("Dictionary after adding 'c':", my_dict)

value_d = my_dict.setdefault('d')
print("Value of 'd':", value_d)
print("Dictionary after adding 'd':", my_dict)