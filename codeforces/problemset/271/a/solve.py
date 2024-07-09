n = str(input())
for i in range(int(n)+1,int(n)+1000):
  if len(set(str(i))) == len(str(i)):
    print(int(i))
    break
