n = int(input())
l, r = [int(i) for i in input().split()]
if n in range(l, r+1):
    print('yes')
else:
    print('no')
