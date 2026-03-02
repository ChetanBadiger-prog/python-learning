#first it will search in local scope than give the output,"inside the inner function is called local scope"
a=10
def outer():
    a=15
    def inner():
        a=20
        print(a)
    inner()
outer()

#than it search enclosed scope so it will print 15 and "in side the outer function is called is enclosed scope"
a=10
def outer():
    a=15
    def inner():
        #a=20
        print(a)
    inner()
outer()

#at the end it search both the local and enclosed if not the value is present than it search in global scope than print the 10,"outside the outer function is called global scope"
a=10
def outer():
    #a=15
    def inner():
        #a=20
        print(a)
    inner()
outer()

#when we comment all the values so it will show an error because there is no such value
# builtinscope