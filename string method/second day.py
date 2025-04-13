text = "gOoD MorNIng addis ABABA"
#str.capitalize converts only the 1st character of entire string to uppercase and the rest lowercase.
capitalized_string = text.capitalize()
print("Original text:", text)
print("capitalized string:", capitalized_string)

#str.swapcase converts uppercase characters of string to lowercase and lowercase characters to uppercase.
swappedcase_string = text.swapcase()
print("Original text:", text)
print("swapcase string:", swappedcase_string)

#str.find is used to search for a substring within a string.
index1 = text.find("addis")
index2 = text.find("ethiopia")
index3 = text.find("D", 3, 10)
index4 = text.find("aBABA")
print("Original text:", text)
print("index 1:", index1)
print("index 2:", index2)
print("index 3:", index3)
print("index 4:", index4)
