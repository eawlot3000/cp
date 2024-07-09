n = int(input())
ret, s = [], 0
for i in range(n):
  ret += [str(input())]
for i in range(len(ret)):
  if ret[i] == 'Icosahedron':
    s += 20
  if ret[i] == 'Cube':
    s += 6
  if ret[i] == 'Tetrahedron':
    s += 4
  if ret[i] == 'Dodecahedron':
    s += 12
  if ret[i] == 'Octahedron':
    s += 8
print(s)
