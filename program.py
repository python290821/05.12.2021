
from Person import Person
from Employee import Employee

# Encapsulation

danny = Person(1, 'danny', 20)
print(danny.name) # print(danny.get_name())
danny.name = '' # danny.set_name('')

e = Employee(2, 'suzi', 21, 40_000)
print(e.name) # getter and setter inherited into derived class