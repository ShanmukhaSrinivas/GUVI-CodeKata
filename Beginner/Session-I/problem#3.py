#Find if given input is vowel or not

class Vowel:
    def find(self,n):
        vowel = "aeiou"
        self.n = n
        if self.n.isalpha():
            if self.n in vowel:
                print('Vowel')
            else:
                print('Consonant')
        else:
            print('invalid')
alpha = input().lower()
obj = Vowel()
obj.find(alpha)
