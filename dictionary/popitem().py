my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

last_item = my_dict.popitem()
print("Removed item:", last_item)
print("Dictionary after popitem():", my_dict)

last_item = my_dict.popitem()
print("Removed item:", last_item)
print("Dictionary after popitem():", my_dict)  

last_item = my_dict.popitem()
print("Removed item:", last_item)

try:
    my_dict.popitem()
except KeyError as e:
    print("Error:", e)