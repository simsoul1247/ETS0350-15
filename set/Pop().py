my_set = {1, 2, 3, 4, 5}

removed_element = my_set.pop()

print("Removed element:", removed_element)
print("Set after pop:", my_set)

removed_element = my_set.pop()
print("Removed element:", removed_element)
print("Set after pop:", my_set)

empty_set = set()
try:
   empty_set.pop()
except KeyError as e:
    print("Error:", e)