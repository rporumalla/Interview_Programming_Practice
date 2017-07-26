# O(n) time complexity
# O(1) space complexity
def isUniqueChars(s):
  if len(s)>128:
    return False
  charSet=[False]*128
  for i in range(len(s)):
    if charSet[ord(s[i])]:
      return False
    charSet[ord(s[i])]=True
  return True

print isUniqueChars('abcdefghijklm')
print isUniqueChars('abcdefgha')
