#num = [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
#num1 = [1, 2, 4, 71, 142]
#print(sum(num), sum(num1))
def divisor(x):
  calc = 0 
  for i in range(1,x):
    if x%i == 0:
      calc += i
  return calc
#print(divisor(220), divisor(284))

#test = 207 306
print(divisor(207), divisor(306))



