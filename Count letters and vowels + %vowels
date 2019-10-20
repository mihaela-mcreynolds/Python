#!/bin/python
from __future__ import division
	
'''Mihaela McReynolds
   p.21 Write a program that reads a word and prints the number of letters 
        in the word, the number of vowels in the word, and the percentage 
        of vowels.
'''

# Get user input
word = raw_input ("Enter a word: ")
# Count letters in user input
length = len(word)
print "Letters: " , length

# Make a list of vowels; look for vowels and count them
vowels = ['a', 'e', 'i', 'o', 'u']
vowelCount = 0

for char in word :
	if char in vowels :
		vowelCount += 1
print "Vowels: ", vowelCount

# Get the percentage of vowels
percent = round((vowelCount/length*100), 2)
print "Percentage of vowels: ", percent
