def bracketValidator(input):
  d = {'(':')', '{':'}', '[':']'}
  openers = d.keys()
  closers = d.values()
  s = []
  for char in input:
    if char in openers:
      s.append(char)
    elif char in closers:
      if not s:
        return False
      else:
	last_unclosed_opener=s.pop()
	if not d[last_unclosed_opener] == char:
	  return False
  return s==[]

print bracketValidator("{ [ ] ( ) }")
print bracketValidator("{ [ ( ] ) }")
print bracketValidator("{ [ }")
