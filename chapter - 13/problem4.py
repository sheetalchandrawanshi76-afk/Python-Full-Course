# Write a program to find the maximum of the numbers in a list using the reduce function.
from funtools import reduce 
l = [1,2,34,53,62,64,65,74,45,55]


def greater(a,b):
    if(a>b):
        return b 

print(reduce(greater, l))    