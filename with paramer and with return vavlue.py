class calculator:
    def __init__(self):
        self.color = 'white'
        self.brand = 'casio'
    def add(self,a,b):
        c=a+b
        return c
c1=calculator()
print(c1.color)
print(c1.brand)
x=10
y=20
result=c1.add(x,y)
print(result)
