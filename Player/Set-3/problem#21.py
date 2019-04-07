#Check if given three points lie on same line
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
z = [int(i) for i in input().split()]
if x[0]==y[0]==z[0] or x[1]==y[1]==z[1]:
    print("yes")
else:
    print("no")
