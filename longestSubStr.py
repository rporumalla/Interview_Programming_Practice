def longSubstr(s):
  start=0
  end=0
  longest=''
  charSet=set()
  while end<len(s):
    end+=1
    if s[end-1] not in charSet:
      charSet.add(s[end-1])
      #print start, end
      #print charSet
      if end-start>len(longest):
        #print 'long: ', longest
 	longest=s[start:end]
      continue
    #print 'b4: ', charSet
    charSet.clear()
    #print 'after: ', charSet
    start=end-1
    end=start

  return longest

print longSubstr('abccdefgh')
print longSubstr('abcadbef')
print longSubstr('abac')
print longSubstr('aaaaa')
