string_1 = 'hlelo'
string_2 = 'hello'

result = ''
for char in string_1:
   if char in string_2 and not char in result:
      result += char

# printing the result
print(result)
