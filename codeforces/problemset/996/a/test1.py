#!/usr/bin/env python3
n = int(input())
c = 0

c += n // 100  # Number of 100 dollar bills
n %= 100       # Remaining amount after withdrawing 100 dollar bills

c += n // 20   # Number of 20 dollar bills
n %= 20        # Remaining amount after withdrawing 20 dollar bills

c += n // 10   # Number of 10 dollar bills
n %= 10        # Remaining amount after withdrawing 10 dollar bills

c += n // 5    # Number of 5 dollar bills
n %= 5         # Remaining amount after withdrawing 5 dollar bills

c += n         # Remaining amount will be withdrawn using 1 dollar bills

print(c)

