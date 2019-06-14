#Divide if the given number divisible by 2
def find(n):
    if n%2 == 0 and n != 0:
        print(int(n/2))
        if ((n/2)%2) != 0:
            return
        else:
            return find(n/2)
    else:
        print(n)
number = int(input())
find(number)
