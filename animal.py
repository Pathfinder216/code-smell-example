class Animal:
    sound: str
    _happiness = 5

    def __init__(self):
        super().__init__()

    def make_sound(self):
        print(self.sound)

    def walk(self):
        self._make_happier()

    def play(self):
        self._make_happier()

    def feed(self):
        self._make_happier()

    def pet(self):
        self._make_happier()

    def _make_happier(self):
        self._happiness += 1

    def is_happy(self):
        raise NotImplementedError


class Cat(Animal):
    """ A simple implementation of a cat """

    sound = "Meow"

    def is_happy(self):
        return False


class Dog(Animal):
    sound = "Bark"

    def is_happy(self):
        return self._happiness > 2
