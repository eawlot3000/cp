#!/usr/bin/env python3
# solve less than 1 min lol
a = str(input())
d = {"A": "T", "T": "A", "C": "G", "G": "C"}
for i in a:
  print(d[i], end="")
