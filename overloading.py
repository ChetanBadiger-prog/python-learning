class A:
    def display(self,a,b,c):
        print(a)
        print(b)
        print(c)
class B:
    def display(self,a,b):
        print(a)
        print(b)
class C:
    def display(self,a):
        print(a)
c1 = C()
c1.display(10)
c1.display(10,20)
c1.display(10,20,30)