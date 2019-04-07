#Print single occurence element

n = int(input())
x = [i for i in input().split()]
s = list(set(x))
l = []
for i in s:
    l.append(x.count(i))
print(s[l.index(1)])
