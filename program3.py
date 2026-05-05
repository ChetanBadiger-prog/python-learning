class hero:
    def __init__(self):
        self.name= "sudeep"
        self.age = 54
        self.numOfMovies = 45
    def act(self):
        print("sudeep is a good actor")
h1 = hero()
print(h1.name)
print(h1.age)
print(h1.numOfMovies)
h1.act()