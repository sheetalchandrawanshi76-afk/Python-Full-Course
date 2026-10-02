# Write a program to print the following star pattern.
# *
# **
# *** for n = 3



'''
for n = 3
*
**
***
 '''
n = int(input("Enter the number: "))
for i in range(1,n+1):
    print(""*(n-1),end="")
    print("*"*i,end="")
    print("\n")