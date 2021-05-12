
class pixel:

    def __init__(self, xCoor=0, yCoor=0, redV=0, greenV=0, blueV=0):
        self.xCoor = xCoor
        self.yCoor = yCoor
        self.redV = redV
        self.greenV = greenV
        self.blueV = blueV

    def set_coords(self, x, y):
        self.xCoor = x
        self.yCoor = y

    def set_grayscale(self):

        averageV = (self.redV + self.greenV + self.blueV) / 3
        averageV = int(round(averageV))

        self.redV = averageV
        self.greenV = averageV
        self.blueV = averageV

    def print_pixel_info(self):
        pixs = (self.redV, self.greenV, self.blueV)

        result = [True for item1 in pixs for item2 in pixs if item1 == 0 if item2 == 0]

        if result == [True, True, True, True]:
            if self.redV > 49:
                pixCol = "red"
            elif self.greenV > 49:
                pixCol = "green"
            elif self.blueV > 49:
                pixCol = "blue"
            else:
                pixCol = ""
        else:
            pixCol = ""


        print("x: " + str(self.xCoor) + ", " + "y: " + str(self.yCoor) + ", " + "Color: " + str(pixs) + " " + pixCol)


def main():
    avivPix = pixel(xCoor=5, yCoor=6, redV=250)
    avivPix.print_pixel_info()
    avivPix.set_grayscale()
    avivPix.print_pixel_info()

main()