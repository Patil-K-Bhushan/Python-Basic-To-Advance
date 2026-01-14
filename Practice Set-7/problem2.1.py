class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Warning: Salary cannot be negative!")
        else:
            self._salary = value


emp = Employee(30000)
print("Initial salary: ", emp.salary)

emp.salary = 45000
print("After positive update: ", emp.salary)

emp.salary = -10000
print("After negative attempt: ", emp.salary)