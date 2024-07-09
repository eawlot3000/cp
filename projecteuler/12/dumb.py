#!/usr/bin/env python3
def tri_nums(n):
  ll = [0]
  for i in range(1, n):
    ll.append(i + ll[i - 1])
  return ll[-1]


def find_500_divisors(n):
  a = tri_nums(n) # the last triangle number to proceed
  count_divisors = 0
  for i in range(1, int(a**0.5) + 1):
    if a % i == 0:
      count_divisors += 2
      if i*i == a:
        count_divisors -= 1
      if count_divisors > 500:
        return count_divisors
  return count_divisors


if __name__ == '__main__':
  num = 1  # Start from the first triangle number.
  while True:
    if find_500_divisors(num) > 500:
      print(f"The first triangle number with over 500 divisors is {tri_nums(num)}")
      break
    num += 1
    if num % 1000 == 0:  # Print progress every 100 steps to monitor performance.
      print(f"Checked up to {num}th triangle number...")



'''
if __name__ == '__main__':
  num = 0
  while True and num < 10000:
    num += 1
    print(num, tri_nums(num), find_500_divisors(num))
    if find_500_divisors(num) > 500:
      print(tri_nums(num))
      '''











#def triangle_numbers(num):
#  return [n * (n + 1) // 2 for n in range(1, num + 1)]
#
#print(triangle_numbers(20))
