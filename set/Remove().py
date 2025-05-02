my_set = {1, 2, 3, 4, 5}

my_set.remove(3)

print("Set after removing 3:", my_set)

try:
    my_set.remove(6)
except KeyError as e:
    print("Error:", e)

print("Final set:", my_set)