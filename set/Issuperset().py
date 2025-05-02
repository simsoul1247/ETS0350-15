set_a = {1, 2, 3, 4, 5}
set_b = {2, 3}
set_c = {6, 7}

result_ab = set_a.issuperset(set_b)
print("Is set_a a superset of set_b?", result_ab)

result_ba = set_b.issuperset(set_a)
print("Is set_b a superset of set_a?", result_ba)

empty_set = set()
result_empty = set_a.issuperset(empty_set)
print("Is set_a a superset of the empty set?", result_empty)