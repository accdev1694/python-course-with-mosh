# STRING METHODS

course = "Python"
# there are functions that are available and specific only to strings
# type in 'course.' and you will see all the in built functions for strings
# these strings are called methods because they are only specific to a particular data type

# everything in python is an object and objects have methods that can be accessed using the dot notation
# when a function is in use inside an object it is called a method

# 1. upper()
# returns all capitals
print(course.upper())                   # PYTHON
# returns a new string hence the original string is still intact
print(course)                           # Python

# 2. lower()
# returns all lowercase

# 3. title()
# return the string with all first characters of each word as a capital

# 4. strip()
# removes all spaces from begining and end of a string
# especially from user input
# lstrip removes from left
# rstrip removes from right

# 5. find()
# returns the index of the first occurence of a string
print(course.find("y"))                 # 1
print(course.find("e"))                 # -1 because e doesnt exist

# 6. replace()
print(course.replace("P", "p"))         # python

# 7. in
# this is an expression
# finds if a character exists in a string
# this returns a boolean value
print("Py" in course)                   # True

# 8. not
# checks to see if a character or a sequence of characters is not found in a string
print("Py" not in course)                   # False
