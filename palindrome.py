def isPalindrome(s):
  return s==s[::-1]

a=123
print isPalindrome(str(a))
b=121
print isPalindrome(str(b))
c='kayak'
print isPalindrome(str(c))
