n = int(input())
summ = 0
height = n*1.5
for i in range(10):
  summ += height
  height = n*1.5
  new_hei = float(height/2)
  height = new_hei
  print(height)
print(summ)


