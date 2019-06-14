n = input()
count = 0
for i in input():
    if (i.isalpha() or i.isdigit()):
        continue
    else:
        count+=1
print(count)
