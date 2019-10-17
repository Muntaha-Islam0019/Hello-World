# Take a name with 3 to 30 chars length, or warn.

name = input("Please enter your name: ")

while len(name) < 3 or len(name) > 50:
    print("A name's length must be more than 2 characters and less than 51 characters.")
    name = input("Please enter your name again: ")

print("Now it's good to go!")
