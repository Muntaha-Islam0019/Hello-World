# Define a type Person, it should have a name attribute and a talk ability.


class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def talk(self):
        print(f"Hi there. I'm {self.last_name}. Nice to meet you")


personOne = Person("Muntaha", "Islam")
personOne.talk()
