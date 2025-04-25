my_tuple = (10, 20, 30, 40, 50, 20)
index_of_twenty = my_tuple.index(20)
print(f"The first occurrence of 20 is at index: {index_of_twenty}")

my_tuple = (10, 20, 30, 40, 50, 20)
index_of_twenty_with_range = my_tuple.index(20, 2)
print(f"The first occurrence of 20 after index 2 is at index: {index_of_twenty_with_range}")