class A:
    def __init__(self):
        self.a=100
class B(A):
    def __init__(self):
        super().__init__()
        self.B=200
class C(B):
    def __init__(self):
        super().__init__()
        self.C=300
c1 = C()
print(c1.a)
print(c1.B)
print(c1.C)