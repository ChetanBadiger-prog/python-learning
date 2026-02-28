class Mobile:
    def __init__(self):
        self.brand="nokia"
    def call(self):
        print("mobile is calling")
    @staticmethod
    def charge():
        print("mobile is charging")
    @classmethod
    def hang(cls):
        print("mobile is hanging")
t1=Mobile()
print(t1.call)
t1.call()
t1.charge()
t1.hang()
Mobile.call(t1)
Mobile.charge()
Mobile.hang()


