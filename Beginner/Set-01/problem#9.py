#Sum of first k number of list
n, k = [int(i) for i in input().split()]
if n>k:
    arr = [int(i) for i in input().split()]
    print(sum(arr[0:k]))
else:
    print("Invalid Input")
    