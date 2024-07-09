a1,a2,n = map(int, input().split())
d = int(a2-a1)
print(int(n*a1 + n*(n-1)*d/2))
