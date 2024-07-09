import sys, math, itertools, functools, collections
input = sys.stdin.readline

def solve(testcase):
    n = input().strip()
    s = 0
    for i in n:
        s = (s+int(i))%9
    s = str((-s)%9)
    if s != '0':
        cur = 0
        l = []
        while cur < len(n) and n[cur] <= s:
            l.append(n[cur])
            cur += 1
        l.append(s)
        while cur < len(n):
            l.append(n[cur])
            cur += 1
    else:
        l = [n[0]]+['0']+list(n[1:])
    print('Case #'+str(testcase)+':', ''.join(l))


for testcase in range(1, int(input())+1):
    solve(testcase)
