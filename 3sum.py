# O(n**2)
def threeSum(myList,n):
  myList=sorted(myList)
  for i in range(len(myList)-2):
    a=myList[i]
    start=i+1
    end=len(myList)-1
    while start<end:
      b=myList[start]
      c=myList[end]
      if a+b+c==n:
	print a,b,c
	end-=1
      elif a+b+c>n:
	end-=1
      else:
	start+=1

lst=[-25,-10,-7,-3,2,4,8,10]
threeSum(lst,0)
print '*************'
threeSum(lst,2)
print '*************'
threeSum(lst,3)
