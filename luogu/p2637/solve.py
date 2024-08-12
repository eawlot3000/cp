#!/usr/bin/env python3
n, m = map(int, input().split())
prices = [int(input()) for _ in range(m)]

prices.sort()
max_profit = 0
best_price = 0

for i in range(m):
  profit = prices[i] * min(n, m - i)
  if profit > max_profit:
    max_profit = profit
    best_price = prices[i]

print(best_price, max_profit)

