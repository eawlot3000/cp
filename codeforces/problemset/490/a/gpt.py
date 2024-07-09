n = int(input())
students = list(map(int, input().split()))

maths = []
programming = []
pe = []

# separate students by their skill
for i in range(n):
  if students[i] == 1:
    programming.append(i+1)
  elif students[i] == 2:
    maths.append(i+1)
  else:
    pe.append(i+1)

num_teams = min(len(maths), len(programming), len(pe))

# output number of teams
print(num_teams)

# output the teams
for i in range(num_teams):
  print(maths[i], programming[i], pe[i])
