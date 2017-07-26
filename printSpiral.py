# O(mXn)
def printSpiral(matrix):
  rows=len(matrix)
  if rows>0:
    k,l=0,0
    cols=len(matrix[0])
    while k<rows and l<cols:
      for i in range(l,cols):
        print matrix[k][i],
      k+=1
      for i in range(k,rows):
        print matrix[i][cols-1],
      cols-=1
      if k<rows:
        for i in range(cols-1,l-1,-1):
	  print matrix[rows-1][i],
        rows-=1
      if l<cols:
        for i in range(rows-1,k-1,-1):
  	  print matrix[i][l],
	l+=1

w,h=8,5
lst=[[i for i in range(w)] for j in range(h)]
print lst
print len(lst)
printSpiral(lst)
