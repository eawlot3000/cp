#!/usr/bin/env python3

# a = "AAAACCCGGT"


with open("rosalind_revc.txt", "r") as f:
  #  a = f.readline().strip()
  a = f.readline().splitlines()

ret = ['q'] * len(a)

for i in range(len(a)):
  if a[i] == 'A':
    ret[i] = 'T'
  elif a[i] == 'T':
    ret[i] = 'A'
  elif a[i] == 'C':
    ret[i] = 'G'
  elif a[i] == 'G':
    ret[i] = 'C'

print("".join(ret)[::-1])



'''
answer:
GCTAGCCAGGTATCGTAAAGTGGCCAGGCGAAATGGTAAACCTGGATTATGATCTGAGTGCCCATATAGACCAGGCCCGTTACGCTTGCGATGAAAATTCCCTAGGCCGCTTGGTCGACTGCAAAGACCTTAGCATTTATACGTGAATGTACAGCCCGTATGTTGCTGGCCGACATTCTCATGCAAGGCATCTTTGCTAAGAAGTGGTCATCCCTGCGCGCATTAGTTCCCACCAACACCGCATTCCCATTCGCGCCGTACAATCAGTCTTAGTGGCGGAAGGATTAGTTGGCGTTTAGACTTGGTGAGTGGAGGATCTAGCCACCCATGCAATGAGCAGTCCTAGTGTGTTGGTTCAGGACCAGGTAACACCCGCCAGGAATGGCGTCATAGTATATTAGCCCTCACTTTTTGCCGTAGAACTAGCCTTGCCGCTACTCCGAGTCGCGTCTGAGAGGACTTTTGTATTTCGAATTTCCTCGGGAGCCACTTTCCTATATTCAGCCGCTGCACCAATCAGAGGTGCGCTTTTAAATGCCCATTCGGATTAGGACGTCCAAGAAGTACGCACTCATTTCAGTGCATACACTACCCGGGGATAGGGCTTACGGATCCAACTTTAATTGCCCAGCGCGCACCCGGTGAGCCACTGCGAGGTAGCCGGGACTCTCAATATCTAGCTGCAGGGCATGGTATTGCTTCTTAAGTGTGAGATATCTCCCCGATTTTTAGGCGCAGAGTCATGCCCAACTGGCCCATCAGATGTGTTAGGGAGTCGGCCAACTGTCGTAGCGGATTATACACTTCAGATATCCGAATTTGAAACCGTATATTGGTGTAGCACAGACAAGGCACGGACTCAAC
'''