'''
n = int(input())
ret = []
ret += map(int, input().split())
aa = sorted(ret)
aa.reverse()
print(aa)
s1, s2 = 0, 0
for i in range(1, n, 2):
  s1 += aa[i-1]
  s2 += aa[i]
print(s1+aa[-1] if len(aa)%2 else s1, s2)


'''

ll = [48, 47, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 33, 32, 31, 29, 28, 27, 26, 25, 24, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 9, 8, 7, 6, 5, 4, 3, 1]

s1, s2 = 0, 0
for i in range(1, 48, 2):
  print(ll[i-1])
  s1 += ll[i-1]
  print(s1)
  print(ll[i])
  s2 += ll[i]
  print(s2)
