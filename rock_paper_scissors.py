#!/usr/bin/env python3

import random

print("Welcome to a game of Rock, Paper, Scissors\n")

rounds = int(input("How many rounds would you like to play: "))

moves = ["rock", "paper", "scissors"]
player = 0
comp = 0

for round in range(rounds):
	print("\nRound " + str(round + 1))
	print("Player: " + str(player) + "\tComputer: " + str(comp))
	rand = random.randint(0, 2) # 0 is rock, 1 is paper, 2 is scissors
	comp_pick = moves[rand]
	player_pick = str(input("Time to pick...rock, paper, scissors: ").strip().lower())

	# game logic
	if player_pick in moves:
		print("\tComputer: " + str(comp_pick))
		print("\tPlayer: " + str(player_pick))
		if player_pick == comp_pick:
			phrase = "It is a tie, how boring!"
			result = "tie"
		elif player_pick == "rock" and comp_pick == "scissors":
			phrase = "Rock smashes scissors!"
			result = "player"
		elif player_pick == "rock" and comp_pick == "paper":
			phrase = "Paper covers rock!"
			result = "computer"
		elif player_pick == "paper" and comp_pick == "scissors":
			phrase = "Scissors cuts paper!"
			result = "computer"
		elif player_pick == "paper" and comp_pick == "rock":
			phrase = "Paper covers rock!"
			result = "player"
		elif player_pick == "scissors" and comp_pick == "rock":
			phrase = "Rock smashes scissors!"
			result = "computer"
		elif player_pick == "scissors" and comp_pick == "paper":
			phrase = "Scissors cuts paper!"
			result = "player"

		print("\t" + phrase)
		if result == 'player':
			print("\tYou win round " + str(round + 1) + ".")
			player += 1
		elif result == 'computer':
			print("\tComputer wins round " + str(round + 1) + ".")
			comp += 1
		else:
			print("\tThis round was a tie.")
	else:
		print("That is not a valid game option!")
		print("Computer gets the point!")
		comp_pick += 1

print("\nFinal Game Results")
print("\tRounds Played: " + str(rounds))
print("\tPlayer Score: " + str(player))
print("\tComputer Score: " + str(comp))
if player > comp:
	print("\tWinner: PLAYER!!!")
elif comp > player:
	print("\tWinner: Computer :-(")