def outer():
    print("inside the outer")
    def inner():
        print("inside the inner")
    inner()
outer()
