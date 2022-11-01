class first:
    def display(self):
        print("first")
class second:
    def display(self):
        print("second")
class third(first,second):
    def display_third(self):
        print("third")

print(third.mro())
x=third()
x.display_third()
x.display()