#!/usr/bin/env python3
a = input()
b = input()
c = input()
print('YES' if sorted(a+b) == sorted(c) else 'NO')
