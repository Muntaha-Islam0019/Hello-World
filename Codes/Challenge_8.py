# Create a guessing game. Computer will set a number,
# the user will have 3 chances to guess.

import random

number = random.randint(1, 10)

print("Guess a number between 1 to 10. You'll have 3 guesses.")

i = 0
while i < 3:
    guess = input("Guess: ")

    if int(guess) == int(number):
        print("You've done it!")
        break
    else:
        print("Try again!")
        i += 1
        if i == 3:
            print(f"You've used your chances. The number I guessed was: {number}")
