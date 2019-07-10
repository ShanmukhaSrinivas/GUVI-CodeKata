k = []
for _ in range(4):
    k.append([int(i) for i in input().split()])
if set(k[1]) == set(k[3]):
    if len(set(k[0])) == 1 and len(set(k[2])) == 1:
        print('yes')
    else:
        print('no')
else:
    print('no')   