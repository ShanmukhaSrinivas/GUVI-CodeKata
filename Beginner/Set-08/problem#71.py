n = input()
if n == ''.join(list(reversed(n))):
    print('yes')
else:
    print('no')
