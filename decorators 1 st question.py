def main():
    print("inside main")
def outer(ptr):
    print("inside outer")
    def inner():
        print("entering inner")
        ptr()
        print("outside outer")
    return inner
ref = outer(main)
ref()