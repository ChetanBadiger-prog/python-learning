class calsi:
    def operations(self,a,b):
        c1 = a+b
        c2 = a-b
        c3 = a*b
        c4 = a/b
        return c1,c2,c3,c4
c = calsi()
r1 = c.operations(5,2)
print(r1)
r1,r2,r3,r4 = c.operations(5,2)
print(r1)
print(r2)
print(r3)
print(r4)
