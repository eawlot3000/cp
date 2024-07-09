n = int(input())
add_num = int(input())
og = str(input()).split()
def swap(a, b):
  temp = a
  a = b
  b = temp
  return a,b

for i in range(add_num):
  if og[-i-1] > og[-i-2]:
    print(swap(og[-i-1], og[-i-2]))


