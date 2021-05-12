
class Animal:

    def __init__(self, name, hunger=0, zoo_name="Hayaton"):
        self.name = name
        self.hunger = hunger
        self.zoo_name = zoo_name


    def get_name(self):
        return self.name

    def is_hungry(self):
        hungry = lambda x: True if x > 0 else False
        return hungry(self.hunger)

    def feed(self):
        if self.is_hungry():
            self.hunger = self.hunger - 1
            # print("wam wam wam")
        else:
            print("I'm not hungry")

    def talk(self, wards):
        print(wards)


class dog(Animal):

    def __init__(self, name, hunger):
        super().__init__(name, hunger)

    def __str__(self):
        return "dog"

    def fetch_stick(self):
        print("There you go, sir!")

    def talk(self):
        super().talk("woof woof")


class cat(Animal):

    def __init__(self, name, hunger):
        super().__init__(name, hunger)

    def __str__(self):
        return "cat"

    def chase_laser(self):
        print("Meeeeow")

    def talk(self):
        super().talk("meow")


class skunk(Animal):

    def __init__(self, name, hunger, stink_count=6):
        super().__init__(name, hunger)
        self.stink_count = stink_count

    def __str__(self):
        return "skunk"

    def stink(self):
        print("Dear lord!")

    def talk(self):
        super().talk("tsssss")


class unicorn(Animal):

    def __init__(self, name, hunger):
        super().__init__(name, hunger)

    def __str__(self):
        return "unicorn"

    def sing(self):
        print("I’m not your toy...")

    def talk(self):
        super().talk("Good day, darling")


class dragon(Animal):

    def __init__(self, name, hunger, color="Green"):
        super().__init__(name, hunger)
        self.color = color

    def __str__(self):
        return "dragon"

    def breath_fire(self):
        print("$@#$#@$")

    def talk(self):
        super().talk("Raaaawr")


if __name__ == '__main__':

    Dog = dog("Brownie", 10)
    Cat = cat("Zelda", 3)
    Skunk = skunk("Stinky", 0)
    Unicorn = unicorn("Keith", 7)
    Dragon = dragon("Lizzy", 1450)

    Dog80 = dog("Doggo", 80)
    Cat80 = cat("Kitty", 80)
    Skunk80 = skunk("Stinky Jr.", 80)
    Unicorn80 = unicorn("Clair", 80)
    Dragon80 = dragon("McFly", 80)

    zooLst = [Dog, Cat, Skunk, Unicorn, Dragon, Dog80, Cat80, Skunk80, Unicorn80, Dragon80]

    for animel in zooLst:
        if animel.is_hungry():
            print(animel, animel.get_name())
        while animel.is_hungry():
            animel.feed()
        animel.talk()

    print(animel.zoo_name)


# print(isinstance(dog, "talk"))