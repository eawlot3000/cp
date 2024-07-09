#!/usr/bin/env python3
#from collections import Counter

#a = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

with open('rosalind_dna.txt', 'r') as file:
    a = file.read().strip()
print(a.count('A'), a.count('C'), a.count('G'), a.count('T'))

#letter_count = Counter(a)
#print(letter_count)
