#!/bin/python
import math
import random

'''Mihaela McReynolds
   2.24 Craps. Write a program that will play several rounds of the popular? 
        dice game known as "craps." The rules of craps are as follows:
	a player rolls a pair of dice. If the sum of the dice is either
	7 or 11 on the first throw, the player wins. If the sum of dice is
	2, 3 or 12 on the first throw, the player loses. Any other sum becomes
	the player's "point." To win, the player must continue rolling the dice 
	until a roll matches the point. This is termed "making the point." If
	the player rolls a 7 before making the point the player loses.
'''

# gamePlaying will be true while game continues
gamePlaying = True
# round counts the number of dice rolls
round = 0
# point gets the sum of the first roll
point = 0
# dice list will hold the two random dice results
dice = []

while gamePlaying == True:
	# get two random ints between 1 and 6
	x = random.randint(1,6)
	y = random.randint(1,6)		
	# dice list gets the results of the dice roll
	dice = [x, y]
	# increment the round
	round += 1
	print dice
	sum = x + y
	# For the first round only, a 7 or 11 wins the game; a 2, 3, or 12 loses the game
	if round == 1:
		if sum in [7, 11]:
			print "Natural! You win!"
			gamePlaying = False
		elif sum == 2:
			print "Snake eyes... Craps! You lose"
			gamePlaying = False
		elif sum == 3:
			print "Ace deuce... Craps! You lose"
			gamePlaying = False
		elif sum == 12:
			print "Boxcars... Craps! You lose"
			gamePlaying = False
		else:
			gamePlaying = True
			# point gets the sum of the first round
			point = sum
			print "Point: ", point
	# For the following rounds, you can win by rolling a sum equal to the point
	else:
		# If you roll 7 before you make the point, you lose
		if sum == 7:
			print "Seven-out! You lose"
			gamePlaying = False
		elif sum == point:
			print "You win!"
			gamePlaying = False 
		else:
			gamePlaying = True
	# Shouldn't be more anywhere near 100 rounds, so break if it gets that high
	if round > 100:
		break
		print "Infinite loop alert!!!"
