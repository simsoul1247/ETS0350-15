numbers = [5, 2, 9, 1, 5, 6]
print("Original list", numbers)
numbers.sort()
print("Sorted list in ascending order:", numbers)
numbers.sort(reverse=True)
print("Sorted list in descending order:", numbers)

fruits = ['mango', 'apple', 'watermelon', 'pineapple', 'banana']
print("Original list", fruits)
fruits.sort()
print("Alphabeticaly sorted list of fruits:", fruits)
fruits.sort(key=len)
print("Sorted list by length:", fruits)