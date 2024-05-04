# FOR LOOPS

# for loops are used to repeat a task a known number of times

# lets send a message to someone 5 times
for number in range(5):
    print('check your email')    
# what is this number? it is of type int and it represents the instances of each iteration

for number in range(1, 6, 2):
    print("check your email", number, number * ".")
# the parameters in range(): start from 1 end before 6 and step of 2
# parameters in the print function: print "check your email" 
# concatinate the number of instances of iteration and with each instance, 
# print dots to match