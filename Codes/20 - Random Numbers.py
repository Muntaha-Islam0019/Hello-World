import random

print(f"This is a random value between 0 and 1: {random.random()}")
print(f"This is a random number between 10"
      f" and 20(inclusive): {random.randint(10, 20)}")

a_list = ["Leviathan", "Suri", "Medusa"]
leader = random.choice(a_list)
print(f"The leader will be: {leader}")