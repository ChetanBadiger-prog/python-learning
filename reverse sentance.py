from shlex import split

# str = "guru is drinking"
# str1 = str.split()
# print(str)
# print(str1)
# for i in reversed(str1):
#     print(i, end=" ")


# another method
# str = input("Enter a string :")
# rev=""
# str1 = str.split()
# for i in str1:
#     rev=i+" "+rev
# print(rev)

# str = input("enter the string")
# rev = ""
# str1 = str.split()
# for i in str1:
#     rev = i+" "+rev
#     print(rev)

str = input("enter string :")
rev = ""
str1 = str.split()
for i in str1:
    rev = i+" "+rev
print(rev)