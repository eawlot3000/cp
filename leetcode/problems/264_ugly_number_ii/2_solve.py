#!/usr/bin/env python3
def nthUglyNumber(self, n: int) -> int:
  # 初始化一个长度为 n 的列表 `l`，用来保存前 n 个丑数
  l = [0] * n
  # 第一个丑数是 1
  l[0] = 1
  
  # 初始化三个指针 a、b 和 c，它们分别指向下一次要与 2、3、5 相乘的丑数
  a = b = c = 0
  
  # 从第 1 个位置开始填充到第 n 个位置
  print(f'in this case, we know n is {n} and l is {l}\n')
  print(f'-'*10)
  for i in range(1, n):
    # 计算三个可能的下一个丑数
    l2 = l[a] * 2
    l3 = l[b] * 3
    l5 = l[c] * 5
    print(f'l2: {l2}, l3: {l3}, l5: {l5}')
    
    # 在三个候选丑数中选取最小的一个作为下一个丑数
    print(f'*before changes, current l is {l}\n')
    l[i] = min(l2, l3, l5)
    print(f'the min of l2, l3, l5 is l[i]=={l[i]}')
    
    # 更新相应指针
    # 如果当前丑数等于 l2，则将指针 a 往前移动一位
    print('and for this round:\n')
    if l2 == l[i]:
      a += 1
      print(f'∵ l2==l[i]\n∴ after movement, a is {a}')
    # 如果当前丑数等于 l3，则将指针 b 往前移动一位
    if l3 == l[i]:
      b += 1
      print(f'∵ l3==l[i]\n∴ after movement, b is {b}')
    # 如果当前丑数等于 l5，则将指针 c 往前移动一位
    if l5 == l[i]:
      c += 1
      print(f'∵ l5==l[i]\n∴ after movement, c is {c}')

    print(f'*after changes, current l is {l}\n')
    print(f'current a is {a}, b is {b}, c is {c}\n')
    print(f'current i is {i}\n')
    print(f'-'*10)
  
  # 返回第 n 个丑数
  return l[n - 1]

print(nthUglyNumber(1, 10))  # 12
