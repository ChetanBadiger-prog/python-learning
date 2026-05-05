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


class person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    def set_name(self,value):
        self.__name = value

    def get_age(self):
        return self.__age
    def set_age(self,value):
        self.__age = value

    name = property(get_name,set_name)
    age = property(get_age,set_age)
p1=person("John",25)
print(p1.name)
print(p1.age)


