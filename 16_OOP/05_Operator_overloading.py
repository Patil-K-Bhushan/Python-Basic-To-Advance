class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overloading the + operator
        #  'other' refers to the object on the *right* side of the +
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self): # String representation (for print() and str())
        return f"({self.x}, {self.y})"

    def __eq__(self, other): # Overloading == operator
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2  # This now works!  It calls p1.__add__(p2)
print(p3)      # Output: (4, 6)  (This uses the __str__ method)

print(p1 == p2) # Output: False (This uses the __eq__ method)


class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Convention: _age indicates it's intended to be "private"

    def get_age(self):  # Getter for age
        return self._age

    def set_age(self, new_age):  # Setter for age
        if new_age >= 0 and new_age <= 150:  # Validation
            self._age = new_age
        else:
            print("Invalid age!")

person = Person("Alice", 30)
print(person.get_age())  # Output: 30

person.set_age(35)
print(person.get_age())  # Output: 35

person.set_age(-5)   # Output: Invalid age!
print(person.get_age())   # Output: 35 (age wasn't changed)



class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Convention: _age for "private" attributes

    @property  # This makes 'age' a property (the getter)
    def age(self):
        return self._age

    @age.setter # This defines the setter for the 'age' property
    def age(self, new_age):
        if new_age >= 0 and new_age <= 150:
            self._age = new_age
        else:
            print("Invalid age!")

person = Person("Bob", 40)
print(person.age)    # Output: 40  (Looks like direct attribute access, but calls the getter)
person.age = 45      # (Calls the setter – looks like attribute assignment)
print(person.age)
person.age = -22 #Output: Invalid age!




class MyClass:
    def __init__(self):
        self._internal_value = 0  #  Convention: _ means "private"

    def get_value(self):
        return self._internal_value

obj = MyClass()
# print(obj._internal_value)  # This *works*, but it's against convention
print(obj.get_value())       # This is the preferred way