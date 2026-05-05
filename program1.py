class fan:
    def __init__(self):
        self.brand = "usha"
        self.color = "white"
        self.cost = 3000
        self.wings = 3
    def on(self):
        print("fan is on")
    def rotate(self):
        print("fan rotate")
    def off(self):
        print("fan off")
fi = fan()
print(fi.brand)
print(fi.color)
print(fi.cost)
fi.on()
fi.rotate()
fi.off()

