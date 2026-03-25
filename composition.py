from os import name


class os:
    def __init__(self):
        self.status = True
        print("os is ready")
    def getos(self):
        print("os is installing")
class mobile:
    def __init__(self, name):
        self.mname = name
        self.o = os()
        print("mobile is ready")
        print("with os installed")
m = mobile("nokia")
print(m.mname)
print(m.o.status)
m.o.getos()
del m
print(m.mname)-



