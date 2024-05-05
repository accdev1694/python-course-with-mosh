# xargs

# if you define a function with just two parameters, 
# but want to call it with more than two arguments, you get an error

def calc(x, y):
     return x + y
 
print(calc(2, 5))
# this works fine

# what if you have more than 2 arguments:
#print(2, 5, 10, 20)     # you get an error

#what you need to do is pass *numbers as paramter for defining the function,
# when you call the function it the returns a tuple with all the argumets
# tuples are iterable, but immutable and numbered
# lets calculate the sum of all the numbers in the argument

def add_num(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
 
print(add_num(2, 5, 100, 20))