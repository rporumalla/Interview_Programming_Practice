# O(log n)
# works only for integer y
def power(x,y):
  if y==0:
    return 1
  #print y
  temp=power(x*1.0,int(float(y)/2))
  if y%2==0:
    return temp*temp
  else:
    if y>0:
      return x*temp*temp
    else:
      return (temp*temp)/x

print power(2,4)
#print power(2,0.5)
print power(3,-4)
#print power(4,-0.5)
#print power(5,0.6)
