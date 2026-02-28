class calculator:
    def __init__(self):
        self.name = "calsi"
        self.color = "blue"
    def add(self,a,b):
        c=a+b
        return c
c1= calculator()
print(c1.name)
print(c1.color)
x=10
y=20
result = c1.add(x,y)
print(result)