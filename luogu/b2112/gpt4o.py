#!/usr/bin/env python3
import sys

input = sys.stdin.read
data = input().strip().split('\n')

num_games = int(data[0])
games = [line.split() for line in data[1:]]

results = []

for player1, player2 in games:
  if player1 == player2:
    results.append("Tie")
  elif (player1 == "Rock" and player2 == "Scissors") or \
       (player1 == "Scissors" and player2 == "Paper") or \
       (player1 == "Paper" and player2 == "Rock"):
    results.append("Player1")
  else:
    results.append("Player2")

for result in results:
  print(result)

