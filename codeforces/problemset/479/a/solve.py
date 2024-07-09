a = int(input())
b = int(input())
c = int(input())
check = []
check += [a+b*c]
check += [a*(b+c)]
check += [a*b*c]
check += [(a+b)*c]
check += [a+b+c]
print(max(check))
