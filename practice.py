# # class book:
# #     def __init__(self,page):
# #         self.pages=page
# # b1=book(100)
# # print(b1.pages)
# # b1.pages=200
# # print(b1.pages)
# # b1.pages=-99
# # print(b1.pages)
#
# # class book:
# #     def __init__(self,page):
# #         self.__pages = page
# # b1=book(5)
# # print(b1._pages)
#
# class book:
#     def __init__(self,page):
#         self.__pages = page
#     def setter(self, value):
#         if value>0:
#             self.__pages = value
#     def getter(self):
#         return self.__pages
#
# b1=book(5)
# res1=b1.getter()
# print(res1)
#
# b1.setter(-99)
# res2=b1.getter()
# print(res2)
#

# s=set()
# for i in range(1,9):
#     number = int(input("enter a number"))
#     s.add(number)
# print(s)

n = int(input("enter a number :"))

i = 1
while (1, n):
    if n % i == 0:
        print("it is a prime number")
        # i = i + 1
        break
    else:
        print("it is not a prime number")

