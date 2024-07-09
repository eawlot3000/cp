'''
s = str(input())
s = s.replace('WUB', ' ')
words = s.split()
out = ' '.join(words)
print(out)
'''

print(' '.join(str(input()).replace('WUB', ' ').split()))
