def isPalindrome(s):
  low=0
  high=len(s)-1
  mid=low+(high-low)/2
  for i in range(0,mid+1):
    if s[i]!=s[high-i]:
      return False
  return True

a=123
print isPalindrome(str(a))
b=121
print isPalindrome(str(b))
c='kayak'
print isPalindrome(str(c))
