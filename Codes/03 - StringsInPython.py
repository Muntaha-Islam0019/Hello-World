# ----- String -----

# Just need to remember one thing here,
# the left side of the colon is your starting index, and,
# the right side of the colon is your ending index + 1.

print("\n")
string = "Hello"
print(string)
print(string[3])
print(string[:])
print(string[0:3])
print(string[-1])
print(string[2:-1] + "\n")

# One can put a string in a variable in 3 different ways.

# First Way:
stringTestOne = 'Voila'  # We can't put ' here.

# Second Way:
stringTestTwo = "It's my pleasure to meet you and you may call me V."

# Third Way:
stringTestThree = ''' 
    *           *
      *       *
        *   *
          *
'''  # Yes, putting 3 ' creates a multiline string.

print(stringTestOne)
print(stringTestTwo)
print(stringTestThree)

# Easy concatenation of string using formatted string
firstName = "Muntaha"
lastName = "Islam"

print(f'''Most {firstName}s are named 'Sidratul {firstName}',
 though, the only boy named '{firstName}' is {firstName} {lastName}.''')  # '/"/three ' can be written after f.

# Python nearly has all the same methods like Java while considering a string.
# For instance ...

print("\n")
aString = "I'm the biggest noob on the universe"
print(len(aString))
print(aString.upper())
print(aString.replace("noob", "stupid"))
print("Pro" in aString)
