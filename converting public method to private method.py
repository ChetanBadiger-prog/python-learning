class dog:
    def __init__(self):
        self.name = "huskey"
    def __bark(self):
        print("dog is barking")
    def helper(self):
        self.__bark()
b1=dog()
b1.helper()