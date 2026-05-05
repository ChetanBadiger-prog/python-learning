# nested deep copy

l = [10,20,["mh","ib"],30]
l1 = l.copy()
print(l)
print(l1)
l[2][1] = "buzz"
print(l)
print(l1)

# achiveing deep copy in nested list

import copy

l = ["10","20",["MH","IB"],"30"]
l1 = copy.deepcopy(l)
print(l)
print(l1)
l[2][1] = "buzz"
print(l)
print(l1)

#
