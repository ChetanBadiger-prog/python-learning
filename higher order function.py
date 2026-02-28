# higher order function and first class function
def func1():
    print("inside the function1")
def func2(ptr):
    print("inside the function2")
    ptr()
    print("learning function2")
func1()
func2(func1)


