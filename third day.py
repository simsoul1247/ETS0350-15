text = "Good Morning Addis Ababa"
#str.index is used to find the first occurrence of a specified substring within a string.
index1 = text.index('a')
index2 = text.index('o')
index3 = text.index("A")
print("original text:", text)
print("index1:", index1)
print("index2:", index2)
print("index3:", index3)

#str.startswith is used to check whether a string starts with a specified prefix (substring).
result1 = text.startswith('Addis')
result2 = text.startswith('good')
result3 = text.startswith('Good')
result4 = text.startswith('Addis', 13, 20)
print("original text:", text)
print("Does the text start with 'Addis'?", result1)
print("Does the text start with 'good'?", result2)
print("Does the text start with 'Good'?", result3)
print("Does the text start with 'Addis' from index 13 to 20?", result4)

#str.endswith is used to check whether a string ends with a specified suffix (substring).
result1 = text.endswith('Ababa')
result2 = text.endswith('Morning')
print("original text:", text)
print("Does the text end with 'Ababa'?", result1)
print("Does the text end with 'Python'?", result2)