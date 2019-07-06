from sys import stdin
n = []
while True:
    if input() != end='\n':
        n.append([int(i) for i in input().split()])
    else:
        break
print(n)
