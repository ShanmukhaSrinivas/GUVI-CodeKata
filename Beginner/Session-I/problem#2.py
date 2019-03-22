#Find if given number is even or odd

class eOrO:
    def find(self,n):
        self.n = n
        assert self.n>0
        if self.n>0 and self.n%2 == 0:
            print('Even')
        elif self.n>0:
            print('Odd')
obj = eOrO()
inp = int(input())
try:
    obj.find(inp)
except Exception:
    print('invalid')
