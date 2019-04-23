#Sort given data
a = [int(i) for i in input().split()]
a.sort()
a = [str(i) for i in a]
print(' '.join(a))
