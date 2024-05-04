# WHILE LOOPS

# repeat something over and over as song as the condition remains true

number = 100
while number > 0:
    print(number)
    number = number // 2
    
# number = 100 is the start point of the iteration
# the iteration will continue to return half of number each time 
# until number is less than 0

# lets create a program wprks like the terminal window for calculating arithmentics

command = ""

while True:       
    command = input(">>> ")
    if command.lower() == "quit":
        break
    num1 = int(input("> "))
    num2 = int(input("> ")) 
    
    if command == "+":
        print(num1 + num2)
    elif command == "-":
        print(num1 - num2)
    elif command == "/":
        print(num1 / num2)
    elif command == "//":
        print(num1 // num2)
    elif command == "*":
        print(num2 * num2)
    elif command == "**":
        print(num1 ** num2)
    elif command == "%":
        print(num1 % num2)
    
    


    

