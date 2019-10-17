class Mammal:
    @staticmethod
    def eat():
        print("Whosh, whposh!")


class Cat(Mammal):
    # 'pass' is redundant, it's just for making someone understand better.
    pass


class Dog(Mammal):
    @staticmethod
    def sound():
        print("Bark, Bark!")


my_dog = Dog
my_dog.eat()
my_dog.sound()

# Though, an object of cat type would return error if sound is called.
my_cat = Cat
# my_cat.sound()
