def func(string):
    k = ''
    LengthOfPalindrome = len(string)
    for i in range(LengthOfPalindrome+1):
        new = string[0:i]
        print(new)
        if len(new) == len(set(new)):
            if len(k) < len(new):
                k = new
    return len(k)


string = input()
print(func(string))
