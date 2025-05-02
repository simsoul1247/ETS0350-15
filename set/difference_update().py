set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print("Original Set A:", set_a)
print("Set B:", set_b)

set_a.difference_update(set_b)
print("Modified Set A after difference_update:", set_a)

set_c = {1, 8}
print("Original Set A:", set_a)

set_a.difference_update(set_b, set_c)
print("Modified Set A after difference_update with multiple sets:", set_a)