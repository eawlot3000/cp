#!/usr/bin/env python3
def count_ways(coins, target):
  # Create a list of zeros, with one extra to account for the zero-index
  ways = [0] * (target + 1)

  # There's 1 way to make 0 with 0 coins
  ways[0] = 1

  # Go through all of the coins
  for coin in coins:
    # For each coin, update the ways count from the coin value up to the target
    for i in range(coin, target + 1):
      ways[i] += ways[i - coin]

  return ways[target]

# Define the coins in pence
coins = [1, 2, 5, 10, 20, 50, 100, 200]

# The target is £2, which is 200 pence
target = 200

# Calculate the number of ways to make £2
count_ways(coins, target)
print(count_ways(coins, target))

