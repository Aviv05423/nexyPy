class TheColorPrint:
    def __init__(self, color=""):

        self.color = color
        self.White = '\033[97m'
        self.Purple = '\033[95m'
        self.Blue = '\033[94m'
        self.Yellow = '\033[93m'
        self.Green = '\033[92m'
        self.Grey = '\033[90m'
        #
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'

        self.Normal = '\033[0m'
        self.Red = '\033[91m'

    def red(self, text):
        print(f"{self.Red}{text}{self.Normal}")

    def white(self, text):
        print(f"{self.White}{text}{self.Normal}")

    def purple(self, text):
        print(f"{self.Purple}{text}{self.Normal}")

    def blue(self, text):
        print(f"{self.Blue}{text}{self.Normal}")

    def yellow(self, text):
        print(f"{self.Yellow}{text}{self.Normal}")

    def green(self, text):
        print(f"{self.Green}{text}{self.Normal}")

    def grey(self, text):
        print(f"{self.Grey}{text}{self.Normal}")

    def bold(self, text):
        print(f"{self.BOLD}{text}{self.Normal}")

    def UNDERLINE(self, text):
        print(f"{self.UNDERLINE}{text}{self.Normal}")

colorPrint = TheColorPrint("none")

# צריך לעשות אימפורט ל-colorPrint
# from color class import colorPrint
# ואז colorPrint נקודה (שם של צבע) וכו'