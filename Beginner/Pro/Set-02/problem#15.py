n = int(input())
List = [int(i) for i in input().split()]
List = sorted(List, key=lambda x: str(bin(int(x)))
              [2:].count('1'), reverse=True)
for i in List:
    print(i)
