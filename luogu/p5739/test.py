# cal: n! (not using loopie!)
def loopie(n):
  if n == 0:
    return 1
  else:
    return n*loopie(n-1)
n = int(input())
print(loopie(n))

'''
# using loopie!
n = int(input())
summ = 1
for i in range(1,n+1):
  summ *= i
print(summ)
'''
