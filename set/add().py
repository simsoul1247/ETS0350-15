my_set = {1, 2, 3}
print("Original set:", my_set)

my_set.add(4)
print("Set after adding 4:", my_set)

my_set.add(2)
print("Set after trying to add 2 again:", my_set)

my_set.add("hello")
print("Set after adding 'hello':", my_set)

my_set.add((5, 6))
print("Set after adding (5, 6):", my_set)