#Palindrome or not
def recur(s,i,fl):
    if l//2>i:
        if s[i] == s[l-i-1]:
            f1 = 0
            recur(s,i+1,f1)
        else:
            f1 = 1
            return f1

s = list(input())
f = 0
l = len(s)
flag = recur(s,0,f)
if flag == 1:
    print("No")
else:
    print("Yes")