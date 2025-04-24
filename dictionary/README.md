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

Get()
It retrieve the value associated with a specified key. 
The primary advantage of using get() over directly accessing the dictionary with square brackets (e.g., dict[key]) is that get() allows you to provide a default value that will be returned if the specified key does not exist in the dictionary. This helps prevent KeyError exceptions.

Items()
It return a view object that displays a list of a dictionary's key-value tuple pairs. 
This method is particularly useful when you need to iterate over both keys and values in a dictionary.

Keys()
It return a view object that displays a list of all the keys in the dictionary. 
This method is useful when you want to access or iterate over just the keys of a dictionary.

Pop() 
It remove a specified key and return the corresponding value. 
If the specified key does not exist, it raises a KeyError unless a default value is provided.