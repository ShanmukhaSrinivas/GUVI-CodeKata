def reverse(s):
  return s[::-1]
def func(string):
  LongestPalindrome = ' '
  LengthOfPalindrome = len(string)
  for i in range(LengthOfPalindrome+1):
    for j in range(LengthOfPalindrome+1):
      if string[i:j] == reverse(string[i:j]):
        if len(LongestPalindrome) < len(string[i:j]):
          LongestPalindrome = string[i:j]
  return len(LongestPalindrome)
string = input()
print(len(string) - func(string))
