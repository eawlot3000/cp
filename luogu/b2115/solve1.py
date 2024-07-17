#!/usr/bin/env python3
import sys

input_text = sys.stdin.read().strip()
decrypted_text = [
  chr(ord(char) - 1) if 'b' <= char <= 'z' else
  'z' if char == 'a' else
  chr(ord(char) - 1) if 'B' <= char <= 'Z' else
  'Z' if char == 'A' else
  char
  for char in input_text
]

print(''.join(decrypted_text))

