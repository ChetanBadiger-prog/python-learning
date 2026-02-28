str = input("Enter a string :")
print(str)
if str.isalpha():
    print("is contain only chracters")
elif str.isdigit():
    print("is contain only digits")
elif str.isalnum():
    print("contains both charac and digits")
else:
    print("other characters")