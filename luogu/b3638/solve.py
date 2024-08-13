#!/usr/bin/env python3
def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
  area = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
  return area // 2

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
print(calculate_triangle_area(x1, y1, x2, y2, x3, y3))
