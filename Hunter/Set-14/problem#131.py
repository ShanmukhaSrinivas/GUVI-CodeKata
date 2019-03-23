#Number series
y = int(input())
x = [int(i) for i in input().split()]
x = sorted(x)
[print(x[-(i+1)],x[i],end = " ") for i in range(int(len(x)/2))]