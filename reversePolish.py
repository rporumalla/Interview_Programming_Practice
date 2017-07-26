def parseRpn(e):
  stack=[]
  for val in e.split(' '):
    if val in ['-','+','*','/']:
      a=stack.pop()
      b=stack.pop()
      if val=='-': result=b-a
      if val=='+': result=b+a
      if val=='*': result=b*a
      if val=='/': result=b/a
      stack.append(result)
    else:
      stack.append(float(val))
  return stack.pop()

if __name__ == '__main__':
  expression='10 3 5 + *'
  res=parseRpn(expression)
  print res
  expression='3 6 + 10 *'
  res=parseRpn(expression)
  print res
