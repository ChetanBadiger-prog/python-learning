class heroine:
    def __init__(self):
        self.name = "rukku"
        self.age = 27
        self.numOfMovies = 7
    def act(self):
        print("rukku is a good actress")
h1 = heroine()
print(h1.name)
print(h1.age)
print(h1.numOfMovies)
h1.act()
h1.adds = "karnataka"
print(h1.adds)
h1.age = 28
# del h1.numOfMovies # if we delete the variable it will show an error.
# print(h1.numOfMovies)