i, j = [int(i) for i in input().split()]
for k in range(i, j+1):
    if k**2 == i*j:
        i = ''
        break
    else:
        continue
if i == '':
    print('yes')
else:
    print('no')
