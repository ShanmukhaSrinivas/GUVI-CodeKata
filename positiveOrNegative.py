
class sign:
    def sig(self,n):
        if n>0:
            print("Positive")
        elif n == 0:
            print("Zero")
        else:
            print("Negative")

obj = sign()
obj.sig(int(input()))