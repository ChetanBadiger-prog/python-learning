class Animal:
    def eat(self):
        print("Animal is eating")
    def sleep(self):
        print("Animal is sleeping")
    def hunt(self):
        print("Animal is hunting")
class lion(Animal):
    pass
class tiger(Animal):
    pass
class fox(Animal):
    pass

l1=lion()
t1=tiger()
f1=fox()
l1.eat()
l1.sleep()
l1.hunt()
t1.eat()
t1.sleep()
t1.hunt()
f1.eat()
f1.sleep()
f1.hunt()

