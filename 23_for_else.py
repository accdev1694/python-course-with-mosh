# FOR_ELSE

# we can break out of a for loop by using a break statement
# but we can also break out using an else statement if the condition is not met
successful = True
for number in range(1, 4):
    print("Attempt", number, "time(s)")
    if successful:
        print("Successful after", number, "time(s)")
        break
else:
    print("Attempted 3 times and failed")
