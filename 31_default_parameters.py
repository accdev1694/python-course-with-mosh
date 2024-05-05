# it is good practice to provide a default parameter to a function
# while defining it so just in case there is no argument given when calling it,  it gets called with the default parameter

def increment(value, by=1):             # a default parameter of 1 is specified
    return value + by


print(increment(21, 5))
# when we print this function, it assumes a the default parameter as the second parameter

# even if a default value is specified, if both arguments are supplied on call, the value in the argument overrides the default parameter
# all the default or optional parameters should come only after the required parameter

