class Employee:
    a = 1 

    @classmethod
    def show(clf):
        print(f"The class value of a is{clf.a}")

e = Employee()
e.a = 45
e.show()
