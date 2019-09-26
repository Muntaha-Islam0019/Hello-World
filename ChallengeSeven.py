# Enhanced weight converter what takes any unit
# (pounds or kgs) and converts to the opposite one.

weight = input("Please enter your weight: ")
unit = input("What is it's unit? ")

if unit.lower() == 'kg' or unit.lower() == 'k' or unit.lower() == 'kgs':
    print(f"Your weight is {round(float(weight) * 2.205, 3)} pounds.")
else:
    print(f"Your weight is {round(float(weight) / 2.205, 3)} KGs.")
