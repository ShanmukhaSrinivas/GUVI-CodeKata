n = int(input())
if n>2:
    for i in range(2,n):
        if n%i == 0:
            print('no')
            break
    else:
        print('yes')
elif n==2:
    print('yes')
else:
    print('no')