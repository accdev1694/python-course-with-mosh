# NESTED LOOPS

# you can nest a loop inside another one
# lets create a 12 times table

for x in range(1, 13):
    for y in range(1, 13):
        print(f"{x} * {y} = {x * y}")
