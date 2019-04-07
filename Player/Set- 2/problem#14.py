#Remove vowels and reverse string
n = int(input())
x = list(input())
for i in x:
    if i.lower() in ['a','e','i','o','u']:
        x.remove(i)
x = ''.join(x)
print(x[::-1])
