#!/usr/bin/env python3
# Python 3 code for Caesar Cipher decryption problem

# Create a translation table for decryption
decryption_table = str.maketrans(
  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
  "zabcdefghijklmnopqrstuvwxyZABCDEFGHIJKLMNOPQRSTUVWXY"
)

# Input the encrypted string
encrypted_string = input()

# Decrypt the string using the translation table
decrypted_string = encrypted_string.translate(decryption_table)

# Print the decrypted string
print(decrypted_string)

