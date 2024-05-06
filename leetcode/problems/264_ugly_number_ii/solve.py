#!/usr/bin/env python3
# this the most efficient solution
import heapq 

def nthUglyNumber(n):
  heap, seen, primes = [], {1}, [2,3,5]
  heapq.heappush(heap, 1)
  for _ in range(n):
    c = heapq.heappop(heap)
    for p in primes:
      new_ugly = c * p
      if new_ugly not in seen:
        seen.add(new_ugly)
        heapq.heappush(heap, new_ugly)
  return c

print(nthUglyNumber(1000000))
