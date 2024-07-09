n, r = map(int, input().split())
ret = []

while True:
  p = n//r
  mod = n%r
  ret += [mod]
  if p == 0:
    break
  n = p
ret.reverse()
out = ''.join(str(i) for i in ret)

print(out)

# for testin
'''
test = int(n, r)
print('the right answer: --> {}'.format(test))
'''
print('----')
print(int('14',8))

