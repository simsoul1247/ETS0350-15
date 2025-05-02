set_a = {11, 12, 13, 14, 15}
set_b = {14, 15, 16, 17, 18}
print("Set A:", set_a)
print("Set B:", set_b)

common_elements = set_a.intersection(set_b)

print("Common elements in Set A and Set B:", common_elements)

set_c = {15, 16, 17}
common_elements = set_a.intersection(set_b, set_c) 