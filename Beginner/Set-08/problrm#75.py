n = list(input())
if len(n) % 2 == 0:
    n[int(len(n)/2)-1], n[int(len(n)/2)] = '*', '*'
else:
    n[int(len(n)/2)] = '*'
print(''.join(n))
