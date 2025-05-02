Set 
Set is an unordered collection of unique elements. 
Sets are mutable, meaning we can add or remove items after the set has been created. 
The built-in `set` type provides several methods that allow us to perform various operations on sets.

Add()
It is used to add a single element to a set. 
If the element already exists in the set, the add() method will not add it again, as sets do not allow duplicate elements.

Clear() 
It is used to remove all elements from a set. 
After calling this method, the set will be empty.

Copy() 
It is used to create a shallow copy of a set. 
This means that it creates a new set that contains the same elements as the original set, but changes made to the new set will not affect the original set, and vice versa.

Difference()
It is used to find the difference between two or more sets. 
It returns a new set that contains all the elements that are present in the first set but not in the other specified sets. 
This method can be particularly useful when you want to determine which elements are unique to a particular set.

Difference_update() 
It is used to remove all elements from a set that are present in another specified set (sets). 
Unlike the difference() method, which returns a new set with the difference, difference_update() modifies the original set in place.

Discard()
It is used to remove an element from a set. 
If the specified element is not present in the set, discard() does nothing and does not raise an error. 
This makes it a safe way to attempt to remove an element without worrying about whether it exists in the set.

Intersection()
It is used to find the common elements between two or more sets. 
It returns a new set containing only the elements that are present in all the sets involved in the intersection.

Intersection_update()
It is used to update a set by keeping only the elements that are present in both the set and one or more specified sets.
 In other words, it modifies the original set to retain only its intersection with the specified sets.

Isdisjoint() 
It is used to determine whether two sets have no elements in common.
It returns True if the sets are disjoint (i.e., they do not share any elements), and False otherwise.

Issubset()
It is used to determine whether a set is a subset of another set.
 A set A is considered a subset of set B if all elements of A are also elements of B. 
The method returns True if A is a subset of B, and False otherwise.

Issuperset() 
It is used to determine whether a set is a superset of another set. 
A set A is considered a superset of set B if all elements of B are also elements of A. 
The method returns True if A is a superset of B, and False otherwise.

Pop()
It is used to remove and return an arbitrary element from the set. 
Since sets are unordered collections, you cannot predict which element will be removed when you call pop().
If the set is empty, calling pop() will raise a KeyError.

Remove() 
It is used to remove a specified element from the set. 
If the specified element is not found in the set, it raises a KeyError. 
Unlike the pop() method, which removes an arbitrary element, remove() requires you to specify the exact element you want to remove.

Symmetric_difference()
It is used to return a new set that contains all the elements that are in either of the two sets, but not in both. 
In other words, it gives you the elements that are unique to each set.
It is useful when you want to find elements that are unique to each of two sets. 
It helps in various scenarios where you need to compare two datasets and identify differences.