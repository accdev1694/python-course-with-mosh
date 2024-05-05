#  kwargs simply mean keyword arguments

def increment(value, by):
    return value + by
    

result = increment(20, 5)
print(result)

# lets shorten this code 
print(increment(20, 5))
# this gives the same result

# we can give a keyword argument 
# to the second parameter just to make the code more readable
print(increment(20, by=5))
# same result, now it sound like saying increment 20 by 5, very readable