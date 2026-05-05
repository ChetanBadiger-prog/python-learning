def outer():
    a = 100
    b= 200
    print(a)
    print(b)
    def inner():
        a=150
        b=250
        print(a)
        print(b)
    print(a)
    inner()
    print(a)
    print(b)
outer()


# non local variable with global variable
# def outer():
#     a = 100
#     b= 200
#     print(a)
#     print(b)
#     def inner():
#         nonlocal a
#         a=150
#         b=250
#         print(a)
#         print(b)
#     print(a)
#     inner()
#     print(a)
#     print(b)
# outer()