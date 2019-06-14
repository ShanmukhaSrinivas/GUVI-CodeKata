n = input()
for i in n:
    if i == '0' or i == '1':
        continue
    else:
        print('no')
        break
else:
    print('yes')