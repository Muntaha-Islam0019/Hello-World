# ----- Taking input and Variable and Conversion -----

name = input("What's your name buddy? ")
print("Hello " + name + "! Welcome to this Repl.")

# Well, like all other languages, Python has variables.
# But, every input is been taken as a String.
# For instance ...

birthYear = input("Please enter your birth-year: ")
print(type(birthYear))

# Now to use this string as an int, one need to define type.
currentYear = input("Please enter current year: ")

print("So, now you're " + str(int(currentYear) - int(birthYear)))
print(type(currentYear))