# Dictionary is a DS which have (key, value) pairs. Like a dictionary, it
# can't have duplicate keys.

student = {
    "name": "Muntaha",
    "age": "19",
    "givenFinal": True
}

# Printing can be done in two ways.
print(student["name"])
print(student.get("age"))

# One can explicitly change the value of one key.
student["name"] = "Moony"
print(student.get("name"))

# This will return an error:
# print(student["birthdate"])

# But, this wont:
print(student.get("birthdate"))

# One can explicitly declare a new key:
student["birthdate"] = "19th of July"
print(student.get("birthdate"))

# One can add a default text while printing from a dictionary. This will be
# printed if the key is not available.
print(student.get("address", "Address is not available."))

