#!/usr/bin/env python3

# equal to this one line..
#print(''.join([i.lower() if i.isupper() else i.upper() for i in str(input())]))

'''
a = str(input())
b = list(i.lower() for i in a if i.isupper())
c = list(i.upper() for i in a if i.islower())
print(''.join(b+c))
'''

print(ord('a')) #-> d
print(ord('b')) #-> e
print(ord('c')) #-> f
print(ord('d')) #-> g
print(ord('x')) #-> a
print(ord('y')) #-> b
print(ord('z')) #->c


#d = {'a':'x', 'b':'y', 'c':'z', 'A':'X', 'B':'Y', 'C':'Z'}

# solved here
d = {'x':'a', 'y':'b', 'z':'c', 'X':'A', 'Y':'B', 'Z':'C'}
a = str(input())
b = ''.join([i.lower() if i.isupper() else i.upper() for i in a])
b = b[::-1]
print(b)

for i in b:
  if i in d:
    print(d[i], end='')
  else:
    print(chr(ord(i)+3), end='')




