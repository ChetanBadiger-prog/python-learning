class person:
    def __init__(self):
        self.__name = "husigiul "
    @property
    def dataaccess(self):
        return self.__name
    @dataaccess.setter
    def dataaccess(self, value):
        self.__name = value
p1 = person()
# p1.dataaccess="chethan"
print(p1.dataaccess)