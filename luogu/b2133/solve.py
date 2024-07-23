#!/usr/bin/env python3
n = int(input())
for my_house in range(1, n + 1):
    total_sum_minus_n = (my_house * 3) + n
    total_houses = 1
    while total_houses * (total_houses + 1) // 2 < total_sum_minus_n:
        total_houses += 1
    if total_houses * (total_houses + 1) // 2 == total_sum_minus_n:
        print(my_house, total_houses)
        break
