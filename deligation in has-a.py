class Radio:
    def turnOn(self,x):
        if x==1:
            print("you turn on")
        else:
            print("you turn off")
class Car:
    def __init__(self,min, max):
        self.min = min
        self.max = max
        self.R = Radio()
C1 = Car(30,140)
print(C1.min)
print(C1.max)
C1.R.turnOn(1)