'''
s = str(input())
print(s)
'''

'''
#2
from sys import stdin, stdout
s = stdin.readline()
stdout.write(str(s))
'''

'''
#3
import sys
def get_ints():
  return map(int, sys.stdin.readline().strip().split())
a,b,c,d = get_ints()
'''

from sys import stdin, stdout
import datetime as dt
start = dt.datetime.now()
n = stdin.readline()
stdout.write(n)
'''
n = input()
print(n)
'''
end = dt.datetime.now()
print("{:.64f}".format((end-start).total_seconds()))
'''
n = stdin.readline()
stdout.write(n)
'''
'''
#aa = stdin.readline()
aa = input()
print(aa)
'''



