#str.isalnum is a built-in string method that checks whether all the characters in a string are alphanumeric
s1 = "Hello1247"
print(s1.isalnum())
s2 = "Hello 1247"
print(s2.isalnum())
s3 = "Hello@1247"
print(s3.isalnum())
s4 = ""
print(s4.isalnum())
s5 = "Hello"
print(s5.isalnum())
s6 = "1247"
print(s6.isalnum())

#str.isspace is used to check whether all the characters in a string are whitespace characters.
A1 = "   "
print(A1.isspace())
A2 = "\n\t  "
print(A2.isspace())
A3 = "  a  "
print(A3.isspace())
A4 = "   1   "
print(A4.isspace())
A5 = ""
print(A5.isspace())
A6 = "\t\t"
print(A6.isspace())

#str.format  is a powerful way to format strings in Python. 
#str.format allows to create strings by embedding values into placeholders defined within the string.
#F-strings, or formatted string literals, were introduced in Python 3.6 as a more concise and readable way to format strings. 
#F-strings allow you to embed expressions inside string literals using curly braces {}.
name = "Dagim"
department = "Electromechanical Engineering"
formatted_string = "My name is {} and I am {} student.".format(name, department)
print(formatted_string)
pi = 3.14159
f,string = f"The value of pi is approximately {pi:.2f}."
print(f,string)
formatted,string = "{:<5} | {:^5} | {:>5}".format('Addis Ababa', 'Ethiopia', 'Africa')
print(formatted,string)
a = 4
b = 8
f-string = f"The sum of {a} and {b} is {a + b}."
print(f-string)