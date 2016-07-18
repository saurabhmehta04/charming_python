'''

A simple example to understand a type of Creational pattern: FACTORY DESIGN PATTERN

'''


class Dog:
    # A simple dog class

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof !"


def get_pet(pet="dog"):
    # A factory method

    pets = {"dog": Dog("hope"), "cat": Cat("Peace")}  # dictionary to store the objects

    return pets[pet]


# new requirement => add cat class.

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Meeow"


c = get_pet("cat")
print(c.speak())
