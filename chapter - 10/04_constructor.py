class Employee:
   language ="Python" # This the class attribute.
   salary = 12000

   def __init__(self,name,salary,language): # dundermethod
      self.name = name
      self.salary = salary
      self.language = language
      print(" I am creating an object")
   
   def getInfo(self):
      print(f"The language is {self.language}.The salary is {self.salary}")

   @staticmethod
   def greet(): 
      print("Good morning")

sheetal = Employee("sheetal", 12000, "Python")
# sheetal.name = "Sheetal"
print(sheetal.name,sheetal.salary,sheetal.language)

# rohan = Employee()


