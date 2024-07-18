#!/usr/bin/env python3
'''
a = str(input()).split() -> return a <list> of strings!
a = str(input().split()) -> return a string!
'''

'''
a = str(input()).split()
print(','.join(str(len(i)) for i in a))
'''

# just this one line!
print(','.join(str(len(i)) for i in str(input()).split()))



'''
print(a)
print(type(a))
print('-----------------')
a = list(input().split())
print(a)
print(type(a))
print('-----------------')
a = input().split()
print(a)
print(type(a))
'''
#print(','.join(str(len(i)) for i in a))
