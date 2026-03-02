from math import pi
# pi=10
def outer():
    # pi=100
    def inner():
        # pi=150
        print(pi)
    inner()
outer()




