#!/usr/bin/env python3
a,b,c = map(int, input().split())

first_max = max(a,b,c)
second_max = min(a+b, b, c)
third_max = min(a, b, b+c)

ret = first_max / second_max * third_max
print(f"{ret:.3f}")
