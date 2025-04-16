my_list = [10, 20, 30, 40, 50, 20]
index_of_twenty = my_list.index(20)
index_of_fifty = my_list.index(50)
try:
    index_of_sixty = my_list.index(60)
except ValueError as e:
    index_of_sixty = str(e)

print("Index of first occurrence of 20:", index_of_twenty)
print("Index of first occurrence of 50:", index_of_fifty)
print("Attempt to find index of 60:", index_of_sixty)