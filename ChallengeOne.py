# Check in a patient's info's for a hospital.

import random

name = input("Please enter your name: ")
age = input("Please enter your age: ")
isNew = input("Are you here for the first time? ")

if isNew.lower() == "yes":
    isNew = True
else:
    isNew = False

if isNew:
    randomId = random.randint(1, 100)
    print(f"Dear {name}({age}), your ID number is:"
          f" {randomId}. Please wait.")
else:
    print(f"Dear {name}({age}), you've been registered with "
          f"your previous ID number. Please wait.")
