# Write a program to input name , marks and phone number of a student and format it using the format function like below:

"The name of the student is harsh ,his marks are 78 and phone number is 87576565"

name = input("Enter name: ")
marks = int(input("Enter marks:"))
phone = int(input("phone number: "))

s = "The name of the student is {} ,his marks are {} and phone number is {}".format (name,marks ,phone)

print(s)
