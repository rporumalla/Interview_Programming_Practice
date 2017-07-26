def countCompression(s):
  if s is None or len(s)==0:
    return 0
  size,count,last=0,1,s[0]
  for i in range(1,len(s)):
    if s[i]==last:
      count+=1
    else:
      last=s[i]
      size+=1+len(str(count))
      count=1
  size+=1+len(str(count))
  return size

def compressString(s):
  size=countCompression(s)
  print 'size:{}'.format(size)
  if size>len(s):
    return s
  last=s[0]
  count=1
  new=''
  for i in range(1,len(s)):
    if s[i]==last:
      count+=1
    else:
      new+=last+str(count)
      count=1
      last=s[i]
  new+=last+str(count)
  return new

print compressString('aabcccccaaa')
print compressString('abcdefghi')
print compressString('abcdefgggh')
