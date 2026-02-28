# accessing the global variable
a = 1000
def func1():
    global a
    print(a)
func1()


# accessing and modifying the global variable
a = 10000
def func2():
    global a
    a = a+15
    print(a)
func2()

