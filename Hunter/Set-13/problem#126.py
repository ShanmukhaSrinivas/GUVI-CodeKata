#Find if sentence is in camel case
n = [i for i in input().split()]
f = 0
for i in n:
    if i[0].isupper():
        continue
    else:
        f = 1
        break
if f == 0:
    print('yes')
else:
    print('no')