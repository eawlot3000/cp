#!/usr/bin/env python3
'''
a = float(input())
og_div = float(1/a)

#print(og_div)
integer_part = int(str(og_div)[0])

if og_div - integer_part <= 10**-6: # [[ <= 1e-6 ]]
  print("YES")
  print(f"1 {integer_part}")
else:
  print("NO")
'''


# latest solution by gpt-4 chatgpt
k = float(input())

# Multiply k by 10^8
p_approx = k * 10**8

# Round p_approx to the nearest integer
p = round(p_approx)

# Set q to 10^8
q = 10**8

# If the error is within the limit
if abs(p/q - k) <= 1e-6:
    print("YES")
    print(p, q)
else:
    print("NO")
