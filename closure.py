#in a nested function calling inner funtion outside the outer function is called closure
def outer():
    a=10
    print(a)
    def inner():
        b=15
        c=20
        d=b+c
        print(d)
    return inner
ref=outer()
ref()

#example 2
def outer():
    print("inside the outer function")
    def inner():
        print("inside the inner function")
    return inner
ref=outer()
ref()
