listOne = [1, 3, 5]
print(listOne)

# Though ...
listTwo = ["Jon", "Kit", "Villain in Advanced Warfare"]
print(listTwo)
# Yes, it prints the strings with a ''

# Lists can be sliced like string too.
a_list = ['a', 'b', 'c', 'd', 'e']
print(f'Full list: {a_list}')
print(f'From 0 till last: {a_list[:]}')
print(f'Can be also done by: {a_list[0:]}')
print(f'Basically it is starting index and ending index + 1.\nFor instance: {a_list[0:2]}')
print(f'Slicing reversely: {a_list[-3:]}. Basically, the position with a negative sign.')

print(f'Slice with step operator: {a_list[::2]}')
# This is basically: starting index:ending index + 1:step
# So ...
print(f'Slicing from 1 with 2 step till 4: {a_list[1:4:2]}')
# Therefore, negative step can return reversed list:
print(f'Reversed list: {a_list[::-1]}')
print(f'Reversed complex list: {a_list[-1:1:-1]}')
# Look carefully, that here it stopped on index 2 and did not visit 1

# Slicing can be done using slice() too. The notation is in the same order.

# One can assign in a list while slicing.
a_list[:2] = ['new', 'elements', 'assignned']
print(f'After assigning with slicing: {a_list}')

# Resizing by slicing:
a_list[:0] = ['some', 'more', 'values', 'what', 'were', 'not', 'there']
print(f'After extending: {a_list}')
# You can shrink it too:
a_list[:10] = ['a', 'b']
print(f'After shrinking: {a_list}')

# Deleting by slicing:
del a_list[3:]
print(f'After deleting: {a_list}')
