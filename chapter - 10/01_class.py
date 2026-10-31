class Employee:
    name ="Sheetal"
    language ="Py" # This the class attribute.
    salary = 12000

sheetal = Employee()
sheetal.name = "Sheetal"
print(sheetal.name,sheetal.language,sheetal.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name,rohan.salary,rohan.language)

# Here name is object attributes and salary and language are class attributes as they directly belong to the class.