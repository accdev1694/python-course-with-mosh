# BUILD CLEANER CODE

# check if an applicant to a university is eligible or not

age = 20
if age > 27:
    print(" Not Eligible")
elif age > 18:
    print("Eligible") 
else:
    print("Not Eligible")
    
# lets use a ternery operator to represent this same code:
message = "Eligible" if 18 < age < 27 else "Not eligible"
print(message)