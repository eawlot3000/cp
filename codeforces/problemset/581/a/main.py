a, b = map(int, input().split())
print(min(a,b), 0 if abs(a-b)//2 <= 0 else abs(a-b)//2)
