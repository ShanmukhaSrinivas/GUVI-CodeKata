x, y = [i for i in input().split()]
count = 0
for i in range(min(len(x), len(y))):
    if x[i] == y[i]:
        continue
    else:
        count += 1
        x = ''.join(list(x).remove(x[i])
print(max(len(x), len(y)) - (i+1) + count)
