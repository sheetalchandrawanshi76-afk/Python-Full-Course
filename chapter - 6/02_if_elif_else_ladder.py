a = int(input("Enter your age:"))

# If elif else ladder.
if(a>=18):
    print("you are above the age of consent") # indentation ko use krke hum if ke ander or else ke ander aa sakte hai jo if ke niche space hai ussi ko indentation khte hai.
    print("Good for you")

elif(a<0):
    print("you are entering an invalid negative age")

elif(a==0):
    print("you are entering 0 which is not a valid age ")

else:
    print("you are below the age of consent") # else statement tabhi execute hoti hai tab upper ki condition true na ho.

print("End of program")