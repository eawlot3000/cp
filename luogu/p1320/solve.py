#!/usr/bin/env python3
# luogu cannot take this input idk why

lines = []
while True:
  line = input()
  if line == "":
    break
  lines.append(line)

single_line = ''.join(lines)
#print(single_line)
N = int(len(single_line) ** 0.5)

code, count = [N], 1
for i in range(1, len(single_line)):
  if single_line[i] == single_line[i-1]:
    count += 1
  else:
    code.append(count)
    count = 1
code.append(count)
print(" ".join(map(str,code)))
