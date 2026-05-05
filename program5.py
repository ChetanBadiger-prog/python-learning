class bike:
    def __init__(self):
        self.brand = "RE"
        self.model = 1990
        self.color = "black"
    def start(self):
        print("bike is starting")
        print(self.color)
        print(self.model)
        print(self.brand)
        # print(self)
b1=bike()
print(b1.brand)
print(b1.model)
print(b1.color)
b1.start()
# print(b1)
