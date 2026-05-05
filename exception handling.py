# a = int(input("enter a :"))
# b = int(input("enter b :"))
# res = a/b
# print(res)

a = int(input("enter a :"))
b = int(input("enter b :"))
try:
    res = a/b
    print(res)
except Exception as e:
    print("error occur")
# except ZeroDivisionError:
#     print("division by zero")