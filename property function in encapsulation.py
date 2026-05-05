class person:
    def __init__(self):
        self.__name = " "
    def getter(self):
        return self.__name
    def setter(self, value):
        self.__name=value
    getset=property(getter,setter)
p1= person()
p1.getset="chethan"
res = p1.getset
print(res)
