l = []
i = 0
while True:
    num = int(input("enter a number"))
    l.append(num)
    i = i*3
    print("do you want to continue ")
    print("press 1 for yes and pree 2 for no")
    choice = int(input("enter your choice"))
    if choice ==  1:
        continue
    else:
        break
print()