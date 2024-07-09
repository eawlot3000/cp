'''
#solution1
s = str(input()).split()
print(int(int(s[0])*0.2 + int(s[1])*0.3 + int(s[2])*0.5))
'''
#solution2 # too SLOW thats same
a,b,c = map(int, input().split())
print(int(a*0.2 + b*0.3 + c*0.5))
