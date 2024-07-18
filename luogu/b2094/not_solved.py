n = int(input())
a = list(map(int, input().split()))
s = max(a)
for i in range(n):
    if a[i] == s:
        a[i] = 0
        break
#a.remove(max(a)) # same: del a[a.index(max(a))]
print(sum(a))
