class Baseclass:
    def __init__(self):
        print("base init")


class Subclass(Baseclass):
    def __init__(self):
        print("welcome")
        Baseclass.__init__(self)

Subclass()


