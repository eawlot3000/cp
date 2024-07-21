#!/usr/bin/env python3
import re
expression = input().strip()
expression = expression.replace(' ', '')
pattern = re.compile(r"(\d+)([\+\-\*/%])(\d+)")
match = pattern.match(expression)

if not match:
  raise ValueError("Invalid expression")

operand1, operator, operand2 = match.groups()
operand1 = int(operand1)
operand2 = int(operand2)

if operator == '+':
  result = operand1 + operand2
elif operator == '-':
  result = operand1 - operand2
elif operator == '*':
  result = operand1 * operand2
elif operator == '/':
  result = operand1 // operand2
elif operator == '%':
  result = operand1 % operand2
else:
  raise ValueError("Invalid operator")

print(result)
