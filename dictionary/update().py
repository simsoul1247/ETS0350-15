dict1 = {'a': 1, 'b': 2, 'c': 3}
print(dict1)
dict2 = {'b': 4, 'd': 5}
print(dict2)
dict1.update(dict2)
print(dict1)

dict3 = {'x': 10, 'y': 20}
print(dict3)
updates = [('y', 30), ('z', 40)]
print(updates)
dict3.update(updates)
print(dict3)