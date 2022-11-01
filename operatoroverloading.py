class sample:
    def set_name(self,name):
        self.name=name

    def __add__(self,other):
        name=self.name+" "+other.name
        return name

First_name=sample()
Second_name=sample()

First_name.set_name("shabeeba")
Second_name.set_name("shamees")

Full_name=First_name+Second_name
print(Full_name)