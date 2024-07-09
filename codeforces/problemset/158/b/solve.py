
n = int(input())
groups = list(map(int, input().split()))
count = [0] * 5
for group in groups:
    count[group] += 1
taxis = count[4] + count[3] + (count[2] * 2 + max(count[1] - count[3], 0) + 3) // 4
print(max(count[1] - count[3], 0))

print(taxis)

