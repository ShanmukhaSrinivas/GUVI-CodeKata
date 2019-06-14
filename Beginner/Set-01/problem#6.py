#Find if given year is leap ot not
n = int(input())
if n > 0:
    if n%4 == 0:
        print("yes")
    else:
        print("no")
else:
    print("invalid")
