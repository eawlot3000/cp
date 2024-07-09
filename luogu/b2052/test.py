'''
#a,b,c = map(int, input().split()), str(input())
#a,b,c = int(input()),int(input()),str(input())
aa = lambda: int(input()) + int(input()) + str(input())
'''

# TODO: figure out how to take int input and string input at the same time 
a,b,c = int(input()), int(input()),  str(input())
if c == '+' or c == '-' or c == '*' or c == '/':
  if c == '+':
    print('{}'.format(a+b))
  if c == '-':
    print('{}'.format(a-b))
  if c == '*':
    print('{}'.format(a*b))
  if c == '/':
    if b != '0':
      print('{}'.format(a/b))
    else:
      print('Divided by zero!')

else:
  print('Invalid operator!')

