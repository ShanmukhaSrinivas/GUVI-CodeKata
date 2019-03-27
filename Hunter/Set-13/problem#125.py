s = input()
sets = sorted(set(s))
for i in sets:
    if s.count(i) == 1:
        print(i,end = '')
