x, y = [int(i) for i in input().split()]
for i in range(x,(x*y)+1):
    if i%x == 0 and i%y ==0:
        print(i)
        break
