n,k=[int(i) for i in input().split()]
c=[int(i) for i in input().split()]
a=int(input())
if a != int(sum(c)/2):
	print("Bon Appetit")
else:
	s=sum(c)-c[k]
	print(int(a-(s/2)))
