#!/usr/bin/env python3
#!/usr/bin/env python3

expression = input().strip()

# Remove spaces from the expression
expression = expression.replace(' ', '')

# Find the operator and operands
if '+' in expression:
  operands = expression.split('+')
  result = int(operands[0]) + int(operands[1])
elif '-' in expression:
  operands = expression.split('-')
  result = int(operands[0]) - int(operands[1])
elif '*' in expression:
  operands = expression.split('*')
  result = int(operands[0]) * int(operands[1])
elif '/' in expression:
  operands = expression.split('/')
  result = int(operands[0]) // int(operands[1])
elif '%' in expression:
  operands = expression.split('%')
  result = int(operands[0]) % int(operands[1])
else:
  raise ValueError("Invalid expression")

print(result)

