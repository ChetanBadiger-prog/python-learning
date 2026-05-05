class  tv:
    def __init__(self):
        self.name="SAMSUNG"
        self.cost=25000
    def display(self):
        self.color="black"
        print(self.color)
t1 =tv()
print(t1.name)
print(t1.cost)
#print(t1.color) it is not inside the constuctor so it is showing an a error.
t1.display()
print(t1.color)
t1.size = 32 #it is in the outside  the class
#there are three types of declaring the variable 1.inside the class and inside the constuctor 2.inside the method and inside the constructor 3.outside the class.
print(t1.size)