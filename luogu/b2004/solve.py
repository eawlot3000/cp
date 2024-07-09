"""
# wrong
a,b,c = list(input().split())

print('{:<8}{:<8}{:<8}'.format(a + b + c))
"""

'''
str = input().split()

for s in str:
  print(s.ljust(8), s.ljust(8), s.ljust(8))
  '''

ret = [(item) for item in input().split()]

'''
for s in ret:
  print(s.ljust(8))
  '''
print('{:<8}'.format(ret[2]))


