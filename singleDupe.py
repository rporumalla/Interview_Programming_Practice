'''
  An array contains n numbers ranging from 0 to n-2. There is exactly one number duplicated in the array. 
  How do you find the duplicated number? For example, if an array with length 5 contains numbers {0, 2, 1, 3, 2}, the duplicated number is 2.
'''

def duplicate(myList):
  sum1=0
  n=len(myList)
  for i in range(n):
    sum1+=myList[i]
  sum2=((n-2)*(n-1))>>1
  return sum1-sum2

lst=[4,0,2,4,1,3]
print duplicate(lst)
