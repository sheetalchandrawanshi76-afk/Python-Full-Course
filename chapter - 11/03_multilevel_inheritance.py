class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a) # print the a attributes 
# print(o.b) # show an erroe as there is no b attributes in Employee class

o  = Programmer()
print(o.a,o.b)

o = Manager()
print(o.a, o.b, o.c)
