L = int(input())
n = [int(i) for i in input().split()]
k = []
for i in n:
	if n.count(i)>1:
		k.append(str(i))
if k == []:
	print('unique')
print(' '.join(sorted(set(k))))
