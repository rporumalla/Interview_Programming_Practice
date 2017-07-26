from stack import Stack

def parse(text):
  chunks=[]
  text=text.replace(' ','')
  for ch in text:
    if ch.isdigit():
      if chunks!=[] and chunks[-1].isdigit():
	chunks[-1]+=ch
      else:
	chunks.append(ch)
    elif ch in '+-/*()':
      chunks.append(ch)

  return chunks

print parse(' 123 + 123 ')
s=Stack()
