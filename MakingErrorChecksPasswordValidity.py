import string

class UsernameErrors(Exception):

    def __init__(self, usernameUrg):
        self.usernameUrg = usernameUrg

# חריגה בשם UsernameContainsIllegalCharacter - מתארת שם משתמש המכיל תווים לא חוקיים.
class UsernameContainsIllegalCharacter(UsernameErrors):

    def __init__(self, usernameUrg, Special):
        self.usernameUrg = usernameUrg
        self.special = Special
        self.specialIndex = self.usernameUrg.index(Special)

    def __str__(self):
        return 'The username "' + self.usernameUrg + '" contains an illegal character "' + self.special + '" at index ' + str(self.specialIndex)

# חריגה בשם UsernameTooShort - מתארת שם משתמש המורכב ממספר תווים קטן מ-3.
class UsernameTooShort(UsernameErrors):

    def __str__(self):
        return 'The username "' + self.usernameUrg + '" is too short'

# חריגה בשם UsernameTooLong - מתארת שם משתמש המורכב ממספר תווים גדול מ-16.
class UsernameTooLong(UsernameErrors):

    def __str__(self):
        return 'The username "' + self.usernameUrg + '" is too long'


class PasswordErrors(Exception):

    def __init__(self, password):
        self.password = password

# חריגה בשם PasswordTooShort - מתארת סיסמה המורכבת ממספר תווים קטן מ-8.
class PasswordTooShort(PasswordErrors):

    def __str__(self):
        return 'The password "' + self.password + '" is too short'

# חריגה בשם PasswordTooLong - מתארת סיסמה המורכבת ממספר תווים גדול מ-40.
class PasswordTooLong(PasswordErrors):

    def __str__(self):
        return 'The password "' + self.password + '" is too long'

class PasswordMissingCharacter(PasswordErrors):
    def __str__(self):
        return 'The password "' + self.password + '" is missing a character'

class PasswardUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super(PasswardUppercase, self).__str__() + " (Uppercase)"

class PasswardLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super(PasswardLowercase, self).__str__() + " (Lowercase)"

class PasswardDigit(PasswordMissingCharacter):
    def __str__(self):
        return super(PasswardDigit, self).__str__() + " (Digit)"

class PasswardSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super(PasswardSpecial, self).__str__() + " (Special)"

def check_input(username, password):
    global _username
    _username = username.replace("_", "")

    global lower
    global upper
    global num
    global Special

    lower = 0
    upper = 0
    num = 0 #.isnumeric()
    Special = 0 #.punctuation

    for i in password:
        if i.islower():
            lower = 1
        elif i.isupper():
            upper = 1
        elif i.isnumeric():
            num = 1
        elif i.partition(string.punctuation):
            Special = 1
        else:
            pass




    listU = list(map(lambda x: x.isalnum(), _username))

    if False in listU:
        global bedLeter
        X = listU.index(False)
        bedLeter = _username[X]

    if not _username.isalnum():
        print(UsernameContainsIllegalCharacter(username, bedLeter))
        # raise UsernameContainsIllegalCharacter(username)

    elif len(username) < 3:
        print(UsernameTooShort(username))

    elif len(username) > 15:
        print(UsernameTooLong(username))


    elif len(password) < 9:
        print(PasswordTooShort(password))

    elif len(password) > 39:
        print(PasswordTooLong(password))

    elif lower <= 0 or upper <= 0 or num <= 0 or Special <= 0:
        if lower <= 0:
            print(PasswardLowercase(password))
        elif upper <= 0:
            print(PasswardUppercase(password))
        elif num <= 0:
            print(PasswardDigit(password))
        elif Special <= 0:
            print(PasswardSpecial(password))

    else:
        print("OK")


if __name__ == '__main__':
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")
