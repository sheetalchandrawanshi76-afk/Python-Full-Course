# Create an empty dictinary . Allow 4 friends to enter there favorite language as value and use key as their names.Assume that the names are unique.

d = {}

name = input("Enter friends name :" )
lang = input("Enter Language name :")
d.update({name: lang})

name = input("Enter friends name :" )
lang = input("Enter Language name :")
d.update({name: lang})

name = input("Enter friends name :" )
lang = input("Enter Language name :")
d.update({name: lang})

name = input("Enter friends name :" )
lang = input("Enter Language name :")
d.update({name: lang})

print(d)