# problem - print 1 to 5 numbers

#for loop
for i in range(1,6):
    print(i)

# while loop
i = 1
while i<=5:
    print(i)
    i +=1

# recursion method
def print_numbers(n):
    if n==0:
        return
    print_numbers(n-1)
print_numbers(5)

#functions method
def print_numbers():
    for i in range(1,6):
        print(i)
print_numbers()

#Oops method
class num:
    def display(self):
        for i in range(1,6):
            print(i)
obj = num()
obj.display()

#list comprehension method
[print(i) for i in range(1,6)]


