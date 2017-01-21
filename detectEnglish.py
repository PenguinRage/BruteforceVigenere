#!/usr/bin/env python

# Detect English Module

# Arg 0 -> python file name
# Arg 1 -> input file to be compared to dictionary
# Arg 2 -> Match score to beat customisable to the length of input per line
import sys

def file_to_list(text_file):
	""" Return text as list """
	with open(text_file, 'r') as f:
		return f.read().splitlines()

def load_dictionary():
	english_words	= {}

	""" Loads dictionary into set """
	with open('sowpods.txt') as f:
		for word in f.read().split('\n'):
			english_words[word] = None
	return english_words

if len(sys.argv) < 3:
    print("Must have the required arguements")
    sys.exit(2)

# Load dictionary
english_words = load_dictionary()

# Load cyphers into list
ciphers	= file_to_list(sys.argv[1])

cipher_count = 0

ciphers_length = len(ciphers)

answer_prospects = ''

# Check ALL dictionary words against ALL cyphers >.<
for cipher in ciphers:
	cipher_count += 1
	match_count = 0
	for word in english_words:
		if word in cipher:
			match_count += 1
	if match_count > int(sys.argv[2]):
		answer_prospects += cipher+'\n'
		print (str(cipher_count) + ' of ' + str(ciphers_length) + ' has ' +  str(match_count) +  ' matches:  ' +  cipher)


# Write to text file
with open('finalanswers.txt', 'w') as myfile:
	myfile.truncate()
	myfile.write(answer_prospects)
