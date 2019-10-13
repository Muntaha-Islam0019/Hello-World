# Price of a house is 1M. If the buyer has good credits, the down payment
# will go down by 10%. Else, it'd go down 20%.

price = 1000000

hasCredits = input("Does the buyer has good credits? ")

if hasCredits.lower() == "yes":
    price *= 0.1
else:
    price *= 0.2

print(f"The down payment is: ${price}")
