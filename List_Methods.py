# Lists are basically lilo.

listOne = [9, 19, 47, 67, 99]

print(listOne)

listOne.append(1)
listOne.remove(99)
listOne.insert(3, 3)

print(listOne)

listOne.append(5)
listOne.append(5)
listOne.append(5)
listOne.append(6)
listOne.append(8)

print(listOne)
print(listOne.count(5))
print(listOne.index(6))

listTwo = listOne.copy()
listTwo.sort()
listTwo.reverse()

print(listOne)
print(listTwo)

listOne.remove(5)
# Just removes the first appearance
print(listOne)
