#!/usr/bin/env python3

n = int(input())
flu_patients = []

for _ in range(n):
  name, temperature, cough = input().split()
  temperature = float(temperature)
  cough = int(cough)
  if temperature >= 37.5 and cough == 1:
    flu_patients.append(name)

for patient in flu_patients:
  print(patient)
print(len(flu_patients))

