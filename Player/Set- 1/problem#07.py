#Reverse even and odd charecters
x = input()
l = len(x)
i = 0
lis = []
while i < l-1:
    lis.append(x[i+1])
    lis.append(x[i])
    i+=2
if l%2 == 0:
    print(''.join(lis))
else:
    lis.append(x[len(x)-1])
    print(''.join(lis))
