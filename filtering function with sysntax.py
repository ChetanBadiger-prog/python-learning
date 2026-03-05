# def even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
l=[]
i=0
while i<=4:
    num=int(input("enter a number :"))
    l.append(num)
    i=i+1
print(l)
# res = list(filter(even,l))
# print(res)
res=list(filter(lambda num:num%2==0,l))
print(res)