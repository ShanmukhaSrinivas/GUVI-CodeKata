#Max element after each insersion
n = [int(i) for i in input().split()]
print(end="\n")
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
l = []
for i in y:
    x.append(i)
    l.append(str(max(x)))
print(' '.join(l))
