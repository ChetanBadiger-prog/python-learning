class A:
    def display(self):
        print(" inside A")
class B(A):
    def display(self):
        print(" inside B")
class C(B):
    def display(self):
        print(" inside C")
        B.display(self)
        A.display(self)
c1 = C()
c1.display()