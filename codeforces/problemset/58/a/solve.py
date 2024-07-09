word, hello, i = input(), 'hello', 0
for letter in word:
  if i < len(hello) and letter == hello[i]:
    i += 1
print('YES' if i == 5 else 'NO')
