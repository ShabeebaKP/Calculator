class Baithunnoor:
    year=2020
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

    def add_age(self):
        self.age=self.age+1

    def relocate(self,place):
        self.place=place

    def display(self):
        print("year"+str(Baithunnoor.year))
        print("name:"+self.name)
        print("age:"+str(self.age))
        print("place:"+self.place)

    @classmethod
    def add_year(cls):
        cls.year = cls.year + 1


x=Baithunnoor("shabeeba",26,"kannur")
y=Baithunnoor("shamees",30,"calicut")

x.display()
y.display()

print("_______________")

Baithunnoor.year=Baithunnoor.year+1

x.add_age()
y.add_age()

x.display()
y.display()

print("_____________________")

Baithunnoor.add_year()

x.add_age()
y.add_age()

x.display()
y.display()
