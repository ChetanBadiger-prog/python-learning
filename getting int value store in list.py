# taking a input from the user and store it in list
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# num3 = int(input("Enter a number: "))
# num4 = int(input("Enter a number: "))
# num5 = int(input("Enter a number: "))
# print(num1,num2,num3,num4,num5)
# list1 = [num1,num2,num3,num4,num5]
# print(list1)

#using the while loop
l=[]
i=0
while i<=4:
    num = int(input("Enter a number: "))
    l.insert(i,num)
    i+=1
print(l)

# store it in vertically
i=0
while i<=4:
    print(l[i])
    i+=1

