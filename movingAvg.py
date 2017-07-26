import itertools
from collections import deque

def moving_average(iterable,n=3):
  it=iter(iterable)
  d=deque(itertools.islice(it,n-1))
  d.appendleft(0)
  s=sum(d)
  for elem in it:
    s+=elem-d.popleft()
    d.append(elem)
    yield s/float(n)

gen=moving_average([40, 30, 50, 46, 39, 44])
for i in gen:
  print i,
