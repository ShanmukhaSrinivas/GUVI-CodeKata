from itertools import combinations
x, y = [i for i in input().split()]
l=[]
per = combinations(x,len(x)-int(y))
for i in per:
    l.append(int(''.join(list(i))))
print(min(l))
