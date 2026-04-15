def fun1():
    print("entering fun1")
    try:
        fun2()
    except Exception as e:
        print("error occured in fun1")
    print("living fun1")
def fun2():
    print("entering fun2")
    try:
        res = 10/0
        print(res)
    except Exception as e:
        print("error occured in fun2")
        raise e
    finally:
        print("living fun2")
print("program start")
fun1()
print("program end")
