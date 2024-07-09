#!/usr/bin/env python3
n, m, k = map(int, input().split())

torches = []
for i in range(m):
  x, y = map(int, input().split())
  torches.append((x, y))

glowstones = []
for i in range(k):
  x, y = map(int, input().split())
  glowstones.append((x, y))

def count_monster_spawns(n, m, k, torches, glowstones):
  monster_spawns = 0
  for i in range(n):
    for j in range(n):
      # Check if (i, j) is not lit by any torch or glowstone
      lit = False
      for x, y in torches:
        if abs(x-i) <= 2 and abs(y-j) <= 2 and ((x == i and abs(y-j) <= 2) or (y == j and abs(x-i) <= 2) or abs(x-i) == abs(y-j) == 2):
          lit = True
          break
      if not lit:
        for x, y in glowstones:
          if abs(x-i) <= 2 and abs(y-j) <= 2:
            if x == i and abs(y-j) <= 1:
              lit = True
              break
            elif y == j and abs(x-i) <= 1:
              lit = True
              break
            elif abs(x-i) == 1 and abs(y-j) == 1:
              lit = True
              break
            elif abs(x-i) == abs(y-j) == 2:
              lit = True
              break
      if not lit:
        # Check if (i, j) is not occupied by any torch or glowstone
        occupied = False
        for x, y in torches + glowstones:
          if x == i and y == j:
            occupied = True
            break
        if not occupied:
          monster_spawns += 1
  return monster_spawns

print(count_monster_spawns(n, m, k, torches, glowstones))

