#!/usr/bin/env python3

# fix

a = input().strip()
for i in a:
  if ord(i) >= 98 and ord(i) <= 122:  # 'b' to 'z'
    print(chr(ord(i) - 1), end="")
  elif ord(i) == 97:  # 'a'
    print("z", end="")
  elif ord(i) >= 66 and ord(i) <= 90:  # 'B' to 'Z'
    print(chr(ord(i) - 1), end="")
  elif ord(i) == 65:  # 'A'
    print("Z", end="")
  else:
    print(i, end="")



'''
print(chr(ord('z')-1))
print(ord('y'))

a = str(input())
for i in a:
  if ord(i) >= 97 and ord(i) <= 121 or ord(i) >= 65 and ord(i) <= 89:
    print(chr(ord(i)-1), end="")
  elif ord(i) == 122:
    print("y", end="")
  elif ord(i) == 90:
    print("Y", end="")
  else:
    print(i, end="")
'''



'''
print(ord("a"))97
print(ord("y")) 121
print(ord("A")) 65
print(ord("Y")) 89
'''
