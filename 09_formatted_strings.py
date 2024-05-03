# FORMATTED STRINGS

# String concatination (+)
first_name = "oloche"
last_name = "aboje"
full_name = first_name + " " + last_name
print(full_name)                            # oloche aboje


# use parameters for the print command
print(first_name, last_name)                # oloche aboje

# formatted strings
full_name = f"{first_name} {last_name}"
print(full_name)                            # oloche aboje

# you can basically add any kind of logic or expression between the curly braces inside the f strings#
