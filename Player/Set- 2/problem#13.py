#Sum of squares of digits
n = int(input())
s = 0
while n>0:
    l = n%10
    n=int(n/10)
    s+=l**2
print(s)
