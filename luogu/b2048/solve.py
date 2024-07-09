# https://www.luogu.com.cn/problem/B2048

import math
'''
weight = int(input())
req = str(input())
'''
weight, req = input().split()
weight = int(weight)

def charge_money():
  if weight <= 1000:
    return charge
  else:
    more_weight = int(weight - 1000)
    more_charge = 4*math.ceil(more_weight / 500)
    return charge+more_charge

# charge = 8
if req == 'y':
  charge = 13
  print(charge_money())

if req == 'n':
  charge = 8
  print(charge_money())





