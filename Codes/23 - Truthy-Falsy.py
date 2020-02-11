a = 0
b = 1
c = 5

if a:
    print(f'ALright, it is {a}')
else:
    print('Ehhe')

if b:
    print(f'ALright, it is {b}')
else:
    print('Ehhe')

if c:
    print(f'Alrigth, it is {c}')
else:
    print('Ehhe')


# Now, Values that evaluate to False are considered Falsy.
# And, Values that evaluate to True are considered Truthy.
# Like, 0, "", () refers to false.
# But, 1, any value, refers to true.

# Likewise, look at this code:
def print_even(data):
	if len(data) > 0:
	    for value in data:
	if value % 2 == 0:
	    print(value)
 	else:
	    print("The argument cannot be empty")


# This can be shortened to: 'if data:'
