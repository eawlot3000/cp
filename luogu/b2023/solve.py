'''
import sys
a,b,c,d = sys.stdin.readlines()
print('{} {} {:.6f} {:.6f}'.format(a,b,float(c),float(d)))
'''

a = str(input())
b = int(input())
c = float(input())
d = float(input())
print('{} {} {:.6f} {:.6f}'.format(a,b,c,d))
