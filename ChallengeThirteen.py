# User will give you number. You'll print each digit in words.

userInput = input("Please enter your number: ")

numbers = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

for digit in userInput:
    print(numbers.get(digit, "This is not a digit."))
