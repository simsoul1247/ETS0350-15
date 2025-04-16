appendex()
Adds an element x to the end of the list.
It modifies the original list in-place.
Only one element can be appended at a time.

extend(iterable)
Adds each element from an iterable (like a list, tuple, set) to the end of the list.
It expands the list instead of nesting the iterable.
Modifies the original list in-place

insert(i, x)
Inserts the element x at index i.
Shifts everything after that index to the right.
Doesn't replace anything — it just slides things over.

remove(x)
Removes the first occurrence of the element x from the list.
If x is not found, Python throws a ValueError.
Only removes one match — not all of them

pop([i])
Removes the element at index i and returns it.
If you don’t give it an index, it pops the last item.
If index is out of range → IndexError.

clear()
Removes all elements from the list.
Leaves you with an empty list.
Doesn’t delete the list itself — just clears it out.

 copy()
 Create a shallow copy of a list.
 Creates a new list that contains references to the same objects as the original list.

count()
Count the number of occurrences of a specified element in a list. 
It returns an integer representing how many times that element appears in the list.

index()
Find the first occurrence of a specified element in a list. 
It returns the index (position) of that element. 
If the element is not found, it raises a ValueError.

reverse()
It reverse the order of the elements in a list in place.
Original list is modified and the elements are rearranged in the opposite order.
It does not return a new list; it simply alters the existing one.

sort()
It sort the elements of a list in ascending order by default.
It modifies the original list in place and does not return a new list. 
It can also customize the sorting order using the reverse parameter and the key parameter.