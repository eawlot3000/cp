n = float(input())
dis, step, count = 2, 2, 1
while dis < n:
  step *= 0.98
  dis += step
  count += 1
print(int(count))
