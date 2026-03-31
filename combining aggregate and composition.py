class heart:
    def __init__(self):
        self.status = "empty"
    def heartattack(self):
        print("person gets heartattack")
class cycle:
    def __init__(self,name):
        self.cname = name
    def buycycle(self):
        print("person gets cycle")
class person:
    def __init__(self,name):
        self.pname =name
        self.h = heart()
        self.c = None
    def hasperson(self,p):
        self.c = p
p1 = person("sundra")
c1 = cycle("herculess")
p1.hasperson(c1)
print(p1.pname)
print(p1.h.status)
p1.h.heartattack()
print(p1.c.cname)
p1.c.buycycle()
del p1
print(c1.cname)
c1.buycycle()
print(p1.h.status)



