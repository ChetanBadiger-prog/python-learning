class former :
    def __init__(self,p , t, r) :
        self.principle=p
        self.time=t
        self.rate=r
    def loan(self) :
        si = (self.principle*self.time*self.rate)/100
        print(si)
f1 = former(200000,4,2.5)
f2 = former(400000,7,2.5)
f1.loan()
f2.loan()