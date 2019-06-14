import math
n = int(input())
k = math.log(n,2)
if math.ceil(k) == math.floor(k):
    print('yes')
else:
    print('no')