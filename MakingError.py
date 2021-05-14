class CustomizedExceptionName(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return "Under 18, his current age is - " + self.age + ", he will be 18 in " + str(18 - int(self.age)) + " years"


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise CustomizedExceptionName(age)
    except CustomizedExceptionName as e:
        print(e)

    else:
        print("You should send an invite to " + name)


send_invitation("Aviv", "14")
