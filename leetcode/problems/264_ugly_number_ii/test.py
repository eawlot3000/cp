#!/usr/bin/env python3
import heapq

def nthUglyNumber(n):
  heap = [] # Min-heap to maintain the smallest ugly numbers
  seen = {1} # A set to keep track of already seen ugly numbers
  heapq.heappush(heap, 1) # Initialize heap with the first ugly number
  
  primes = [2, 3, 5] # Prime factors for ugly numbers
  
  # Extract the minimum element from the heap n times
  for _ in range(n):
    current = heapq.heappop(heap)
    print(type(current), current)
    # Add new ugly numbers by multiplying current with each prime factor
    for prime in primes:
      new_ugly = current * prime
      print(current, prime, new_ugly)
      print(f'now seen: {seen}')
      if new_ugly not in seen:
        seen.add(new_ugly)
        heapq.heappush(heap, new_ugly)
        print(f'after seen: {seen}, and heap: {heap}')
    print('---')

  
  return current

# Example usage:
n = 100000
print(nthUglyNumber(n))  # Output: 12
