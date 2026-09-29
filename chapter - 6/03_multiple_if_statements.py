a = int(input("Enter your age:"))

# If statement no: 1
if(a%2 == 0):
     print("a is even")

 # End of If statement no: 1    

# If statement no: 2    
if(a>=18):
    print("you are above the age of consent") # indentation ko use krke hum if ke ander or else ke ander aa sakte hai jo if ke niche space hai ussi ko indentation khte hai.
    print("Good for you")

elif(a<0):
    print("you are entering an invalid negative age")

else:
    print("you are below the age of consent")
# End of If statement no: 2

print("End of program")