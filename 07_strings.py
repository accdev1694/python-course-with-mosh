# STRINGS

course = "Python"
# use double or single quotesbut keep it consistent

# you can also use tripple quotes for really lont text:
message = '''
Hello, i would really love to see you tonight

this is really urgent
'''

    # INBUILT FUNCTIONS
# functions are reusable lines of code

# 1. len
# gets the length of a string
# in built functions are onlt called to ne used sinced they are already defined inside python
print(len(course))  # 6

# 2. indexing
# square brackets are used for indexing
print(course[0])                # P
print(course[-1])               # n (last index)
print([-2])                     # o (second character from end)

# you can slice strings as well
print(course[0:3])              # Pyt (excluded the last character in the slice)

print(course[0:])               # Python (index 0 to end)

print(course[:3])               # Pyth (prints from index 0 to 3 excluding 3)

print(course[:])                # Python (clones entire string)