#Count of perfect squares
x, y =[int(i) for i in input().split()]
count =0
for i in range(y+1):
    k = i*i
    if k in range(x,y):
            count+=1
print(count)
