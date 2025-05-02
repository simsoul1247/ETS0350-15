set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print("Set A:", set_a)
print("Set B:", set_b)

common_elements = set_a.intersection(set_b)

print("Common elements in Set A and Set B:", common_elements)

set_c = {5, 6, 7}
common_elements = set_a.intersection(set_b, set_c)