#Max common element in the input
x = []
l = []
n = int(input())
for i in range(n):
    x.append(input())
for i in range(min(len(x[0]),len(x[1]))):
    if x[0][i] == x[1][i]:
            l.append(x[0][i])

print(l)