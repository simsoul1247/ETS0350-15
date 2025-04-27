original_set = {1, 2, 3, 4, 5}
print("Original set:", original_set)

copied_set = original_set.copy()
print("Copied set:", copied_set)

copied_set.add(6)
print("After adding to copied set:")
print("Original set:", original_set)
print("Copied set:", copied_set)