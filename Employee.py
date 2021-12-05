from Person import Person

class Employee(Person):
    def __init__(self, id, name, age, salary):
        Person.__init__(self, id, name ,age)
        self.salary = salary



