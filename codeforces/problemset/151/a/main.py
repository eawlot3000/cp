n = []
n += map(int, input().split())
drink = n[1] * n[2] / n[-2]
lime = n[3] * n[4]
salt = n[5]/n[-1]
print(int(min(drink,lime,salt)/n[0]))
