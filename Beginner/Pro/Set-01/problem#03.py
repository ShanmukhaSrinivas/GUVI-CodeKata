x, y = [i for i in input().split()]
for i in x:
        for j in y:
                if i == j:
                        continue
                else:
                        break
        else:
                break
k = y.index(j)
if k == 0:
        print(len(y))
else:
        print(len(y)-(k+2))