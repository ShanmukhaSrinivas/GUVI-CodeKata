i, j = [int(i) for i in input().split()]
for k in range(min(i, j), max(i, j)+1):
    if k**2 == i*j:
        i = ''
        break
    else:
        continue
if i == '':
    print('yes')
else:
    print('no')
