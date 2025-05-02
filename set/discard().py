my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

my_set.discard(3)
print("Set after discarding 3:", my_set)

my_set.discard(6)
print("Set after trying to discard 6 (which does not exist):", my_set)