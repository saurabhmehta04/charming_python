class Dog:
    # one of the objects to be returned

    def speak(self):
        return "Wooof"

    def __str__(self):
        return "Dog"


class DogFactory:
    # concrete factory

    def get_pet(self):
        return Dog()

    def get_food(self):
        return "Dog Food !"


class PetStore:
    # Abstract Factory method

    def __init__(self, pet_factory=None):
        # pet factory is our abstract factory
        self._pet_factory = pet_factory

    def show_pet(self):
        # Utility method to display the details of the objects returned by the DogFactory
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'".format(pet_food))


# create a concrete factory
factory = DogFactory()

# create a pet store housing our Abstract factory
shop = PetStore(factory)

# Invoke the utility method to show the details of the pet
shop.show_pet()
