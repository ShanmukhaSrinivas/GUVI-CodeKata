#Maximum occurence of a charecter
x = input()
s = list(set(x))
l = []
for i in s:
    l.append(x.count(i))
print(s[l.index(max(l))])
