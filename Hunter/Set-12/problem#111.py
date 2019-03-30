#Add diagonal elements
n = int(input())
k = 0
mat = [[int(j) for j in input().split()]for i in range(n)]
for i in range(n):
    k += mat[i][i]
print(k)