# Remove duplicates in a list.

a_List = [1, 1, 2, 1, 3, 5, 5, 8, 1, 3]
a_Unique_List = []

for item in a_List:
    if item not in a_Unique_List:
        a_Unique_List.append(item)

print(a_Unique_List)
