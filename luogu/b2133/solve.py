#!/usr/bin/env python3
n = int(input())

for my_house in range(1, n + 1):
    # Solve for total_houses using the rearranged formula
    total_sum_minus_n = (my_house * 3) + n
    # To find total_houses, we need to solve the equation: total_houses * (total_houses + 1) / 2 = total_sum_minus_n
    # We use a while loop to find when this equation holds
    total_houses = 1
    while total_houses * (total_houses + 1) // 2 < total_sum_minus_n:
        total_houses += 1
    if total_houses * (total_houses + 1) // 2 == total_sum_minus_n:
        print(my_house, total_houses)
        break

