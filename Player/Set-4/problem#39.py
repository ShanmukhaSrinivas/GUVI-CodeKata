#Check if given number is power of 2
import math as m
n = int(input())
l = m.log(n)/m.log(2)
if l in range(0,n):
    print("yes")
else:
    print("no")
