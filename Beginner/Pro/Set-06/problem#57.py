#Minimum 2 charecters in both strings
n, m = [set(i) for i in input().split()]
count = 0
for i in n:
    for j in m:
        if i == j:
            count+=1
print(count)
if count >= 2:
    print("yes")
else:
    print("no")
