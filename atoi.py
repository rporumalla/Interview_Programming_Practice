def atoi(string):
  if not string and len(string)<1:
    return None
  flag=1
  j=0
  result=0
  if string[0]=='-':
    flag=-1
    j+=1
  for i in range(j,len(string)):
    result=result*10+(ord(string[i])-ord('0'))
  return result*flag    

if __name__ == '__main__':
  print atoi('89789')
  print atoi('-123')    
