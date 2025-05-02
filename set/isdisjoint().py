set_a = {1, 2, 3}
set_b = {4, 5, 6}
set_c = {3, 7, 8}

result_ab = set_a.isdisjoint(set_b)
print("Are set_a and set_b disjoint?", result_ab)

result_ac = set_a.isdisjoint(set_c)
print("Are set_a and set_c disjoint?", result_ac)