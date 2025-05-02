set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
set_c = {2, 3, 6}

result_ab = set_a.issubset(set_b)
print("Is set_a a subset of set_b?", result_ab)

result_ac = set_c.issubset(set_a)
print("Is set_c a subset of set_a?", result_ac)

empty_set = set()
result_empty = empty_set.issubset(set_b)
print("Is the empty set a subset of set_b?", result_empty)