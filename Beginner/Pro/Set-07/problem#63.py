def func(string):
    k = ''
    Length = len(string)
    for i in range(Length+1):
        new = string[0:i]
        if len(new) == len(set(new)):
            if len(k) < len(new):
                k = new
    return len(k)


string = input()
print(func(string))
