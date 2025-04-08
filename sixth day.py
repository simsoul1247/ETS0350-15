#str.join is used to concatenate a sequence of strings (like a list or a tuple) into a single string, with a specified separator between each element.
words = ['Hello', 'Good', 'Morning', 'Addis', 'Ababa']
sentence1 = ' '.join(words)
print("Original text:", words)
print(sentence1)
sentence2 = ', '.join(words)
print(sentence2)

#str.isalpha is used to check if all the characters in a string are alphabetic (i.e., letters).
s1 = "Hello"
print(s1.isalpha())  
s2 = "Hello Addis Ababa"
print(s2.isalpha())
s3 = "Hello1247"
print(s3.isalpha()) 
s4 = ""
print(s4.isalpha())
s5 = "Café"
print(s5.isalpha())
s6 = "Hello!"
print(s6.isalpha())  

#str.isdigit is used to check if all the characters in a string are digits (i.e., numeric characters).
N1 = "1247"
print(N1.isdigit()) 
N2 = "12 47"
print(N2.isdigit())
N3 = "Hello1247"
print(N3.isdigit())
N4 = "1247!"
print(N4.isdigit())
N5 = ""
print(N5.isdigit())
print(s6.isdigit())
N6 = "124.7"
print(N6.isdigit()) 
N7 = "-1247"
print(N7.isdigit())  