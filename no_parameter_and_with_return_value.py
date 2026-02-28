class calculator:
    def __init__(self):
        self.color = "black"
        self.brand = "casio"
    def add(self):
        a=10
        b=20
        c=a+b
        print(c)
        return c
c1=calculator()
print(c1.color)
print(c1.brand)
result = c1.add()
print(result)