#Paragram
n = input().lower()
l = list(" abcdefghijklmnopqrstuvwxyz")
l1 = list("abcdefghijklmnopqrstuvwxyz")
s = sorted(set(n))
if s==l or s==l1:
    print("yes")
else:
    print("no")
