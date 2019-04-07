#Lower case to Upper case and vice versa
x = input()
for i in x:
    if i.isupper():
        print(i.lower(),end="")
    else:
        print(i.upper(),end="")
