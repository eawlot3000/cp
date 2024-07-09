n = int(input())

name, age, grade = [], [], []
for i in range(n):
  info = str(input())
  name += [info[i]]
  age += [info[i+1]]
  grade += [info[i+2]]
  info = 0

for i in range(n):
  if int(grade[i]) >= 600:
    grade[i] = 600
  print(name[i], int(agnamee[i]), int(grade[i])*1.2)
