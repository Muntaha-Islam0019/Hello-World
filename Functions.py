def name_maker(first_name, last_name):
    print(f"{last_name}, {first_name}")


# Adding 2 blank lines after and before method is a convention.

# Arguments can be passed in two ways:

# Positional Arguments:
name_maker("Muntaha", "Islam")

# Keyword Arguments:
name_maker(last_name="Islam", first_name="Anik")

# When using both of them together, put positional args at first; or, an
# error will occur.
name_maker("Romulus", last_name="Lupin")


# Every function returns 'None' unless you modify it.
def height_converter(height_in_inches):
    return height_in_inches / 39.37


print(height_converter(345))

# This will return a None as the name is already
# printed by the function itself.
print(name_maker("test", "name"))
