#!/usr/bin/env python3
word = input().strip()

if word.endswith('ing'):
  word = word[:-3]
elif word.endswith('ly') or word.endswith('er'):
  word = word[:-2]
print(word)


'''
word = input().strip()
word = word[:-3] if word.endswith('ing') else word[:-2] if word.endswith('ly') or word.endswith('er') else word
print(word)
'''
