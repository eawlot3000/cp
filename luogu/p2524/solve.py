#!/usr/bin/env python3
import itertools

def find_lexicographic_rank():
  import sys
  input = sys.stdin.read
  data = input().split()
  
  N = int(data[0])
  X = data[1]
  
  perms = sorted(itertools.permutations(range(1, N + 1)))
  target = tuple(map(int, list(X)))
  
  rank = perms.index(target) + 1
  print(rank)

find_lexicographic_rank()

