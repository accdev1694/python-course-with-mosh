# COMPARISON OPERATORS

print(10 > 3)               # True
print(10 == "10")           # False
print(10 != "10")           # True

print("bag" > "apple")      # True (when sorted, bag comes after so its considered greater)
print("bag" == "BAG")       # False
print("bag" > "BAG")        # True
print("bag" > "Bag")        # True

# you can check the numeric representation of characters
print(ord("b"))             # 98
print(ord("B"))             # 66
# this is why b is greater than B

