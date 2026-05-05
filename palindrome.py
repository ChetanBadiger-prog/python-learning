# str = input("Enter a string :")
# rev = ""
# for i in str:
#     rev = i+rev
# if str == rev:
#     print("is palindrome")
# else:
#     print("is not palindrome")


str = input("enter the string :")
rev = ""
for i in str:
    rev = i+rev
if rev==str:
    print("the string is palindrome")
else:
    print("the string is not palindrome")