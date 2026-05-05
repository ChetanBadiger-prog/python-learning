a = 20000000000000 #global variable which it is stored in global space
def func1():
    a = 100
    b=200
    print(a)
    print(b)
def func2():
    c = 500
    print(a)# it is the global variable
    print(c)
func1()
func2()