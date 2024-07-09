player = input()
count = 1
danger = False
for i in range(1, len(player)):
  if player[i] == player[i-1]:
    count += 1
    if count >= 7:
      danger = True
      break
  else:
    count = 1
print("YES" if danger else "NO")
