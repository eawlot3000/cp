#!/usr/bin/env python3
m, n = map(int, input().split())

image1 = []
for _ in range(m):
  row = list(map(int, input().split()))
  image1.append(row)

image2 = []
for _ in range(m):
  row = list(map(int, input().split()))
  image2.append(row)


similar_pixel = 0
all_pixel = m*n

for i in range(m):
  for j in range(n):
    if image1[i][j] == image2[i][j]:
      similar_pixel += 1
print(f"{(similar_pixel/all_pixel)*100:.2f}")
