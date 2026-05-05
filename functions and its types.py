# no parameter no return value
def add():
    a=10
    b=20
    c=a+b
    print(c)
add()

# with parameter with return value
def add(a,b):
    c=a+b
    return c
a = add(100,20)
print(a)

# with parameter no return value
def add():
    a=5
    b=10
    return a+b
r=add()
print(r)
print(add())

#