n = int(input())
ret = []
for i in range(n):
  a,b = map(int, input().split())
  s = abs(a-b)
  if s%10==0:
    ret += [int(s/10)]
  else:
    ret += [int(s/10)+1 if s/10.0000 == float(s/10) else int( (s/10)+1)]
print(*ret, sep='\n')
