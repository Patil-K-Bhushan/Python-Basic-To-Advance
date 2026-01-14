class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printPerson(self):
        print("Name: ", self.name + ", Age: ", self.age)

p1 = Person("Bhushan", 20)

print("Name: ", p1.name)
print("Age: ", p1.age)

p1.printPerson()