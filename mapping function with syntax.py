# def add(num):
#     return num+10
l=[]
i=0
while i<=4:
    num=int(input("Enter a number:"))
    l.append(num)
    i=i+1
    print(l)
    res=list(map(add,l))
    print(res)

