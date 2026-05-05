#1. diffrent approches to write a reverse list

# using reverse method
lst = [1,0,2,0,3,0,4]
lst.reverse()
print(lst)

#
l = [1,2,3,4,5,6]
m = len(l)
res = []
for i in range(m-1, -1, -1):
    res.append(l[i])
print(res)


l = [1,2,3,4,5,6]
res = []
for x in l:
    res.insert(0, x)
print(res)


lst = [1,0,2,0,3,0,4]
reversed_lst = []
for i in range(len(lst)-1, -1, -1):
    reversed_lst.append(lst[i])
print(reversed_lst)


l = [1,2,3,4,5,6]
m = len(l)
for i in range(m // 2):
    l[i], l[m-1-i] = l[m-1-i], l[i]
print(l)


l = [1,2,3,4,5,6]
res = []
while l:
    res.append(l.pop())
print(res)


l = [1,2,3,4,5,6]
res = []
for _ in range(len(l)):
    res.append(l.pop())
print(res)  # [6, 5, 4, 3, 2, 1]


def reverse_list(lst):
    if not lst:
        return []
    return reverse_list(lst[1:]) + [lst[0]]
l = [1,2,3,4,5,6]
print(reverse_list(l))


def reverse_list(lst):
    if not lst:
        return []
    return reverse_list(lst[1:]) + [lst[0]]
l = [1,2,3,4,5,6]
print(reverse_list(l))

#slicing method
l = [0,1,2,3,4,5,6]
res = l[::-1]
print(res)

#using reverse
l = [1,2,3,4,5,6]
l.reverse()
print(l)

l = [1,2,3,4,5,6]
res = list(reversed(l))
print(res)





