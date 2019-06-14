k = input()
def digit():
    return any(i.isdigit() for i in k)
def char():
    return any(i.isalpha() for i in k)
if digit() and char():
    print('Yes')
else:
    print('No')
