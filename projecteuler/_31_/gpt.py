def count_ways(coins, target):
  # Create a list of zeros, with one extra to account for the zero-index
  ways = [0] * (target + 1)

  # There's 1 way to make 0 with 0 coins
  ways[0] = 1

  # Go through all of the coins
  for coin in coins:
    # For each coin, update the ways count from the coin value up to the target
    for i in range(coin, target + 1):
      # Update the count for this value
      ways[i] += ways[i - coin]
      # Print the current state after processing this coin value
      print(f'After processing coin {coin}p, ways to make {i}p: {ways[i]}')
      
  return ways[target]

# Define the coins in pence
coins = [1, 2, 5, 10, 20, 50, 100, 200]

# The target is £2, which is 200 pence
target = 200

# Calculate the number of ways to make £2
total_ways = count_ways(coins, target)

# Print the total number of ways to make £2
print(f'Total ways to make £2: {total_ways}')

