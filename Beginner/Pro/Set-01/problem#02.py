from itertools import permutations
x, y = [i for i in input().split()]
l=[]
per = permutations(x,len(x)-int(y))
for i in per:
    l.append(int(''.join(list(i))))
print(min(l))
