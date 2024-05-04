# LOGICAL OPERATORS
# and or and not

# lets create a n application to check if applicants are eligible for a loan
good_credit = True
high_income = False
student = False


# lets use a ternery operator
message = "eligible" if high_income and good_credit and not student else "Not eligible"
print(message)

# with the and operator, the statement returns true only if noth conditions are true
# for the or operator, if any one condition is false, then the entire statement returns false
# the not operator sets the status of student to true as students are not eligible for this loan


# lets implement a condition where the person can have a low income, good credit and a student to be eligible
message = "Eligible" if (good_credit or high_income) and not student else "not elegible"
print(message)