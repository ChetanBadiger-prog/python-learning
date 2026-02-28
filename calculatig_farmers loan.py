class Former:
    r= 2.5
    def __init__(self,p,t):
        self.principle=p
        self.time=t
    def loan(self):
        si = (self.principle*self.time*Former.r)
        print(si)
f1 = Former(200000,4)
f2 = Former(500000,7)
f3 = Former(400000,7)
f1.loan()
f2.loan()
f3.loan()
print(Former.r)