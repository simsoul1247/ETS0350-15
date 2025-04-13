#str.lstrip is used to remove leading whitespace(other specified characters) from the left side of a string.
text1 = "   Hello, Good Morning Addis Ababa? Have a Good Day   "
string1 = text1.lstrip()
print("Original text:", text1)
print("Stripped string 1:", string1)
text2 = "!!!Hello, Good Morning Addis Ababa? Have a Good Day!!!"
string2 = text2.lstrip("!")
print("Original text:", text2)
print("Stripped string 2:", string2)
text3 = "Hello, Good Morning Addis Ababa? Have a Good Day"
string3 = text3.lstrip("Hello,")
print("Original text:", text3)
print("Stripped string 3:", string3)

#str.rstrip is used to remove any trailing characters (characters at the end of a string).
text1 = "   Hello, Good Morning Addis Ababa? Have a Good Day   "
string1 = text1.rstrip()
print("Original text:", text1)
print("Stripped string 1:", string1)
text2 = "Hello, Good Morning Addis Ababa? Have a Good Day!!!"
string2 = text2.rstrip("!")
print("Original text:", text2)
print("Stripped string 2:", string2)
text3 = "Hello, Good Morning Addis Ababa? Have a Good Day Bye"
string3 = text3.rstrip("Bye")
print("Original text:", text3)
print("Stripped string 3:", string3)

#str.split is used to divide a string into a list of substrings based on a specified delimiter.
textA = "Hello, Good Morning Addis Ababa? Have a Good Day"
word1 = textA.split()
print("Original text:", textA)
print("Splitted words", word1)
textB = "Hello, Good, Morning, Addis, Ababa?, Have, a, Good, Day"
word2 = textB.split(",")
print("Original text:", textB)
print("Splitted words", word2)
textC = "Hello, Good Morning Addis Ababa? Have a Good Day"
word3 = textC.split(" ", 5)
print("Original text:", textC)
print("Splitted words", word3)