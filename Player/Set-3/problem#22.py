#Greatest number dividing both given values
max = 0
x, y = [int(i) for i in input().split()]
for i in range(1,y+1):
    if (x%i == 0 and y%i == 0) and i > max:
        max = i
print(max)
