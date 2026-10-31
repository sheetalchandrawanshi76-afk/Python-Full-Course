class Employee:
   language ="Python" # This the class attribute.
   salary = 12000

   def getInfo(self):
      print(f"The language is {self.language}.The salary is {self.salary}")

   def greet(self): 
      print("Good morning")

sheetal = Employee()
# sheetal.language = "javaScript"
sheetal.greet()
sheetal.getInfo()
# Employee.getInfo(sheetal)

