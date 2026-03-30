class charger :
    def __init__(self,name) :
        self.cname=name
    def getcharger(self) :
        print("Charger is working")
class mobile :
    def __init__(self,name) :
        self.mname=name
        self.c = ""
    def hasmobile(self,p) :
        self.c=p
m1 = mobile("IQ")
c = charger("C pin")
m1.hasmobile(c)
print(m1.mname)
print(m1.c.cname)
m1.c.getcharger()
del m1
print(c.cname)
c.getcharger()

# program2
class charger:
    def __init__(self,name):
        self.cname = name
    def getcharger(self):
        print("charger is working")
class mobile:
    def __init__(self,name):
        self.mname = name
        self.c = ""
    def hasmobile(self,p):
        self.c = p
m1 = mobile("samsung")
c = charger("cpin")
print(m1.mname)
print(c.cname)
m1.c.getcharger()
del m1
print(c.cname)
c.getcharger()


