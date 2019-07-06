k = input()
l = int(len(k)/2)
f = 0
for i in range(l):
    for j in range(len(k)-1,l+1):
        if k[i] == k[j]:
            continue
        else:
            f = 1
            break
    else:
        break
if f == 0:
    print('yes')
else:
    print('no')
