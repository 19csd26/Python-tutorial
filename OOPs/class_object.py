class person:
    counter = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        person.counter += 1
    def __init__(self,name = "ram",age = "20"):
        self.name = name
        self.age = age

    def ShowInfo(self):
        print('name:', self.name, end= " ")
        print('age:', self.age)

    def Cupcake(self):
        print('I am a Cupcake')

    @classmethod
    def ShowCount(cls):
        print('count:', cls.counter)

p1 = person()
p1.ShowInfo()
p2 = person(name = "sam")
p2.ShowInfo()
p3 = person(name = "ravi", age = "20")
p3.ShowInfo()
p4= person()
p4.Cupcake()