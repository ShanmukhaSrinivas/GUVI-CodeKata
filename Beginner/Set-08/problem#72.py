n = input()
k = 'aeiou'
for i in k:
    if i in n:
        n = ''
        break
    else:
        continue
if n == '':
    print('yes')
else:
    print('no')
