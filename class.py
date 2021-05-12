
class dog:
    count_animals = 0
    def __init__(self, name = "fred"):
        self.name = name
        self.age = 4
        dog.count_animals += 1

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def birthday(self):
        self.age = self.age + 1

    def get_age(self):
        return self.age

def main():
    an1 = dog("hi")
    an2 = dog()
    an1.set_name("fredi")
    print(an1.get_name())
    print(an2.name)
    print(dog.count_animals)


main()