def func(string):
    k = ''
    LengthOfPalindrome = len(string)
    for i in range(LengthOfPalindrome+1):
        for j in range(LengthOfPalindrome+1):
            new = string[i:j]
            if len(new) == len(set(new)):
                if len(k) < len(new):
                    k = new
    return len(k)


string = input()
print(func(string))
