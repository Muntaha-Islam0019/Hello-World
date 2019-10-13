try:
    user_input = input("Please enter a number: ")
    print(f"So, you've entered: {int(user_input)}")
    print("Let's try to divide it by zero.")
    print(int(user_input) / 0)
except ValueError:
    print("I asked for a number!")
except ZeroDivisionError:
    print("You can't divide something by zero!")
