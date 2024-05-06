#!/usr/bin/env python3
# Follow up: Could you solve it without converting the integer to a string?

def isPalindrome(x):
    if x < 0:
        return False
    if x == 0:
        return True
    if x % 10 == 0:
        return False
    reversed_num = 0
    print(f'x: {x}, reversed_num: {reversed_num}')
    while x > reversed_num:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
        print(f'loopie: x: {x}, reversed_num: {reversed_num}')

    print('\nafter while loop, x is now <= reversed_num, so')
    print(f'x is {x}, reversed_num is {reversed_num}, reversed_num // 10 is {reversed_num // 10}, are they equal? {x == reversed_num or x == reversed_num // 10}')
    return x == reversed_num or x == reversed_num // 10

result = isPalindrome(121)
print(result)
