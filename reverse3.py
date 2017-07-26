def reverse(s):
  s=list(s)
  if s:
    start=0
    end=len(s)-1
    while start<end:
      s[start],s[end]=s[end],s[start]
      start+=1
      end-=1
    return ''.join(s)
  return None


a=123
print reverse(str(a))
print str(a)==reverse(str(a))
a='kayak'
print reverse(str(a))
print a==reverse(a)
a=121
print str(a)==reverse(str(a))
a='quick brown fox'
print reverse(a)
print a==reverse(a)  
print reverse('abcde')
print reverse('abcdef')
