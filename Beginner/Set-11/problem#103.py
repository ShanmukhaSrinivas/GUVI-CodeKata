#Lowercase to Uppercase
n = [i for i in input().split()]
l = []
for i in n:
    l.append(i[0].upper()+i[1:])
[print(l[i],end=" ") for i in range(len(l)-1)]
print(l[len(l)-1])