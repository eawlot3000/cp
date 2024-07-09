n = int(input())
s = str(input()).split()
summ = 0
for i in s:
  summ += int(i)
print("{:.12f}".format(summ/n))
