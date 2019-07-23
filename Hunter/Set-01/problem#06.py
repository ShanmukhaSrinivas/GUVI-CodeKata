l = int(input())
l = 'unique'
k = [int(i) for i in input()]
for i in k:
    if k.count(i) > 1:
        l = i
print(l)
