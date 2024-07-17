#!/usr/bin/env python3


d = {'x':'a', 'y':'b', 'z':'c', 'X':'A', 'Y':'B', 'Z':'C'}
a = ''.join([i.lower() if i.isupper() else i.upper() for i in str(input())])[::-1]

# Create a list from the generator expression and join it to a single string
result = ''.join(d[i] if i in d else chr(ord(i)+3) for i in a)
print(result)

# this is wrong!
#print(d[i] if i in d else chr(ord(i)+3) for i in a)
# this is correct. use this:
#print(''.join(d[i] if i in d else chr(ord(i)+3) for i in a))

