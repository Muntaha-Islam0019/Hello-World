# This code is related to 'Shop' package.

# Yes, one need to mention the package name before
# importing a module from a package.
from Codes.Shop.Prices import price

cart = ["shirt", "pant", "shoe"]
total_price = 0

for product in cart:
    total_price += price(product)

print(total_price)
