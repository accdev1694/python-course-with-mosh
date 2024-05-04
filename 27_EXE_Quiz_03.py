# WRITE A PROGRAM THAT PRINTS ALL EVEN NUMBERS FROM 1 TO 10

# my range below has three parameters:
# first is the start point of the loop
# second is the end point of loop, excluding the end index 10
# third is the step, every 2
count = 0
for num in range(2,10,2):
    count += 1
    print(num)
print(f"We have {count} even numbers")