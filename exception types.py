from logging import exception

try:
    a = int(input("enter a number :"))
    b = int(input("enter a number :"))
    result = a/b
    print(result)
except (ValueError,ZeroDivisionError) as e:
    print("it is a value error or division by zero")
# except  as e:
#     print("division by zero")
except Exception as e:
    print("error occured")
