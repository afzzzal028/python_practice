#lower() method converts all uppercase characters in a string into lowercase characters and returns it.
text = "Hello, World!"
print(text.lower())

#upper() method converts all lowercase characters in a string into uppercase characters and returns it.
print(text.upper())

#capitalize() method converts the first character of a string into uppercase and returns it.
print(text.capitalize())

text ="I am learning Python."
print(text.replace("Python", "Java"))  #replace() method replaces a specified phrase with another specified phrase and returns the modified string.

print(text.split())  #split() method splits a string into a list where each word is a list item.

words=["Python", "is", "awesome"]
print(" ".join(words))  #join() method takes all items in an iterable and joins them into one string.

print(text.find("Python"))  #find() method searches the string for a specified value and returns the position of where it was found.

fruits= "apple, apple, banana, cherry, apple"
print(fruits.count("apple"))  #count() method returns the number of times a specified value occurs in a string.

text= "        Afzal       "
print(text.strip())  #strip() method removes any whitespace from the beginning or the end of a string.

text= "Afzal"
print(text.startswith("A"))  #startswith() method returns True if the string starts with the specified value.

print(text.endswith("l"))  #endswith() method returns True if the string ends with the specified value.

text = "  Machine Learning with Python  "

# 1. String length
print(len(text))

# 2. Indexing
print(text[0])

# 3. Slicing
print(text[0:7])

# 4. Membership
print("Python" in text)

# 5. String formatting
name = "Afzal"
score = 95
print(f"{name} scored {score}")

''' 
One important concept: strings are immutable. 
Methods such as replace() and lower() return new strings rather than modifying the original string.
'''