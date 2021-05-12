class colorPrint:
    def __init__(self):
        self.Normal = '\033[0m'

        # White: '\033[97m',
        # Purple: '\033[95m',
        # Blue: '\033[94m',
        # Yellow: '\033[93m',
        # Green: '\033[92m',
        # Red: '\033[91m',
        # Grey: '\033[90m',
        # Normal: '\033[0m',
        # BOLD: '\033[1m',
        # UNDERLINE: '\033[4m',

        # Clist = {"White": '\033[97m',
        #          "Purple": '\033[95m',
        #          "Blue": '\033[94m',
        #          "Yellow": '\033[93m',
        #          'Green': '\033[92m',
        #          "Red": '\033[91m',
        #          "Grey": '\033[90m',
        #          "Normal": '\033[0m',
        #          'BOLD': '\033[1m',
        #          "UNDERLINE": '\033[4m'}


    def printColor(self, color, text):
        Clist = {"White": '\033[97m',
                 "Purple": '\033[95m',
                 "Blue": '\033[94m',
                 "Yellow": '\033[93m',
                 'Green': '\033[92m',
                 "Red": '\033[91m',
                 "Grey": '\033[90m',
                 "Normal": '\033[0m',
                 'BOLD': '\033[1m',
                 "UNDERLINE": '\033[4m'}

        print(f"{Clist[color]}{text}{self.Normal}")

color = colorPrint()
color.printColor("Green", "asdsd")
