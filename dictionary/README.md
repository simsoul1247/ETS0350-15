Dictionary 
Dictionaries are a built-in data type that store key-value pairs. 
They come with a variety of methods that allow you to manipulate and interact with the data they contain.

Clear()  
It is used to remove all items from the dictionary, effectively making it an empty dictionary. 
It does not take any parameters and does not return any value. 
After calling clear(), the dictionary will still exist but will contain no key-value pairs.

Copy() 
It is used to create a shallow copy of the dictionary. 
A shallow copy means that it creates a new dictionary object with the same key-value pairs as the original dictionary, but it does not create copies of the objects that are referenced by the keys and values. 
Instead, it copies references to those objects.

Fromkeys()
It is a class method that creates a new dictionary from a given sequence of keys and an optional value. 
It initializes the new dictionary with the specified keys, each associated with the same value (which defaults to None if not provided).
