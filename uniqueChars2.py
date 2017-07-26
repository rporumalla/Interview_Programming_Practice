# O(n) time complexity
# O(1) space complexity
def isUniqueChars2(s):
  checker=0
  for i in range(len(s)):
    val=ord(s[i])-ord('a')
    if checker & (1<<val) > 0:
      return False
    checker |= 1<<val
  return True

print isUniqueChars2('abcdefghijklm')
print isUniqueChars2('abcdefgha')
print isUniqueChars2('ababcdcde')
