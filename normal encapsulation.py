class person():
    def __init__(self):
        self.__person = " "
    def setter(self, value):
        self.__person = value
    def getter(self):
        return self.__person
p1 = person()
p1.setter("chethan")
res = p1.getter()
print(res)
