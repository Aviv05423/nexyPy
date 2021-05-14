
class BigThing:

    def __init__(self, name, variable):
        self.name = name
        self.variable = variable

    def size(self):
        if isinstance(self.variable, int):
            return self.variable
        else:
            return len(self.variable)

class BigCat(BigThing):
    def size(self):
        size = super().size()
        if size > 20:
            return "very fat"
        elif size > 15:
            return "fat"
        else:
            return "OK"



if __name__ == '__main__':
        cutie = BigCat("mitzy", 22)

        print(cutie.size())