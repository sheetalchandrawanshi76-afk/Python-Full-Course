# Write a class 'Complex' to represent complex numbers, along with overloaded operators '+' and '*' which add multiplies them.

class Complex :
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def __add__(self ,c2):
        return Complex(self.real + c2.real , self.imag + c2.imag)

    def __mul__(self ,c2):
        return Complex(self.real * c2.real , self.imag * c2.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = Complex(1,2)
c2 = Complex(3,4)
print(c1 + c2)
print(c1 * c2)
