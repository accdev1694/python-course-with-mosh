# let us create that greet functions again and return a value

def greet(first_name, last_name):
    return(f"{first_name}, {last_name}")


#store that value returned into a variable
greet_person = greet("oloche", "aboje")
print(greet_person)

# this way you can easily use this new variable in 
# a number of ways, even in a different file

# if we had printed instead of returning a value, the function is only good for printing that value

