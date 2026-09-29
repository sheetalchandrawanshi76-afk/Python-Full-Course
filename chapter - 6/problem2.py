# Write a problem to find out wheather a student has passed or failed if it requires a total if 40% and at least 33% in each subject to passed. Assume 3 subject and take a marks as an input from the user.
      
marks1 = int(input("Enter Marks 1 :"))
marks2 = int(input("Enter Marks 2 :"))
marks3 = int(input("Enter Marks 3 :"))

# Check fot total percentage
total_percentage = (100*(marks1 + marks2 + marks3)) /300
if(total_percentage>=40 and marks1>33 and marks2>33 and marks3>33):
    print("you are passed:",total_percentage)

else:
      print("you failed , try again next year:", total_percentage)
