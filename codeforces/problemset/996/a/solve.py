#!/usr/bin/env python3
n = int(input())
c = 0

c += n // 100
n %= 100 

c += n // 20 
n %= 20      

c += n // 10 
n %= 10      

c += n // 5  
n %= 5       

c += n       

print(c)

