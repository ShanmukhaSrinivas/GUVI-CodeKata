#Removal of spaces
x = list(input())
while True:
    if " " in x:
        x.remove(" ")
    else:
        break
print(''.join(x))
