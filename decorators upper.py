def main():
    str = "pentagon"
    return str
def outer(ptr):
    print("inside the outer")
    def inner():
        print("entering inner")
        res= ptr()
        ans=res.upper()
        print(ans)
        print("inside outer")
    return inner
ref=outer(main)
ref()



