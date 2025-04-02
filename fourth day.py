text = "Good Morning Addis Ababa? Have a Good Day!"
#str.count is used to count the number of occurrences of a substring within a string.
count1 = text.count("Good")
count2 = text.count("Good", 0, 12)
count3 = text.count("DAY")
count4 = text.count("night")
print("original text:", text)
print(f"The word 'Good' exists {count1} times in the sentence.")  
print(f"The word 'Good' exists {count2} time in the sentece before '?' mark.")
print(f"The word 'DAY' exists {count3} times in the sentence.")
print(f"The word 'night' exists {count3} times in the sentence.")

#str.replace is used to replace occurrences of a specified substring with another substring in a string.
new_text1 = text.replace("Morning", "Afternoon")
new_text2 = text.replace("Good", "nice", 2)
new_text3 = text.replace("evening", "night")
new_text4 = text.replace("Addis Ababa", "")
print("original text:", text)
print(new_text1)
print(new_text2)
print(new_text3)
print(new_text4)

#str.strip is used to remove leading and trailing whitespace (spaces, tabs, newlines, etc.) from a string.
text1 = text.strip('!')
print("original text:", text)
print(text1)