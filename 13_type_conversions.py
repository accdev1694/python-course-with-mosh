# TYPE CASTING

# the input function is used to get a value from the user
x = int(input("x: "))               # wrap with an int function
y = x + 1
print(y)                
# you must convert the value of input to int or float since every input function returns a string

# you can check the type of a variable
print(type(y))                  # class "int"

# in python there are truthy or falsy values
# falsy: "", 0, None
# truthy: everything else
print(bool(""))                 # False
print(bool(None))               # False
print(bool(0))                  # False
print(bool(-20))                # True
print(bool(20))                # True

# convert an integer to a float
print(float(20))                # 20.0

# convert a float to an integer
print(int(20.5))                # 20
