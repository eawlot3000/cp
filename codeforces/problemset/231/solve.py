n = int(input())
cnt = 0
for i in range(n):
  s = map(int, input().split())
  if sum(s) >= 2:
    cnt += 1
print(cnt) 
