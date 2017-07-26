def window(s,size=3):
  i=iter(s)
  win=[]
  for e in range(0,size):
    win.append(next(i))
  yield win
  for e in i:
    #print e
    win=win[1:]+[e]
    yield win

w=window('abcdefghi',9)
for x in w:
  print x

"""
['a', 'b']
['b', 'c']
['c', 'd']
['d', 'e']
['e', 'f']
['f', 'g']
['g', 'h']
['h', 'i']
"""

"""
['a', 'b', 'c']
['b', 'c', 'd']
['c', 'd', 'e']
['d', 'e', 'f']
['e', 'f', 'g']
['f', 'g', 'h']
['g', 'h', 'i']
"""
