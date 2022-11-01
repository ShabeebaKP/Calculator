class Baseclass:
    def display(self):
        print("hello")

class subclass(Baseclass):
    def display1(self):
        print("hai")

x=Baseclass()
y=subclass()



y.display1()