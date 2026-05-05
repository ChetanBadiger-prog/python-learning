#  shallow copy

l = ["10","20","30","40","90"]
l1 = l
print(l)
print(l1)
print(l[2])
l[2]=300
print(l)
print(l1)

# deep copy

l = [10,20,33,40,50]
l1 = l.copy()
print(l)
print(l)
del l[2]
print(l)
print(l1)