#!/usr/bin/env python

import string, re
from collections import Counter
from itertools import cycle

#SUBS
def fileLen(textFile):
    with open(textFile) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def fileToText(textFile):
	""" Return text from file specified """
	with open(textFile, 'r') as myfile:
		return myfile.read()

def fileToList(textFile):
	""" Return text as list """
	with open(textFile, 'r') as myfile:
		return myfile.read().splitlines()

def hugeCleanString(rawString):
	""" Return string with no punctuation, no spaces, all caps """
	return ''.join(filter(str.isalpha, rawString.lower()))

def twinsIndex(cipherString):
	""" Returns the twin index of a string """
	cipherStringLength  = len(cipherString)
	twinsCount			= 0.0
	# Get twinsies, ONLY A to Z, NO overlapping twinsies like 'xxx'
	regex = re.compile(r'([A-Z])\1')
	for match in regex.finditer(cipherString):
		twinsCount += 1

	# Do math, get twIndex :3
	return twinsCount / ( cipherStringLength-1 ) * 26

# Define alphabet
alphabet = map(chr, range( ord('a'), ord('z')+1))

# Get the cipher text
cipherText = hugeCleanString(fileToText('cipher.txt'))

# Import SOWPODS into a list
sowpodsList = fileToList('sowpods.txt')

# Get file length
sowpodsLength = fileLen('sowpods.txt')
decryptedOut = ''
decryptCount = 0

for sowpodsItem in sowpodsList:
	# Create a tuple of cipherCharacter, keyCharacter
	KeyCipherTuple	= zip(cipherText, cycle(sowpodsItem))
	decipheredResult = ''
	frequencyCountRaw = 0
	cypherFrequencySum = 0.0

	for KeyCipherTupleValues in KeyCipherTuple:
		decipheredTemp = reduce(lambda x, y: alphabet.index(x) - alphabet.index(y), KeyCipherTupleValues)
		decipheredResult += alphabet[decipheredTemp % 26]

	# Let's do some frequency analysis on each line maybe?
	frequencyCountRaw = Counter(decipheredResult)
	cypherLength = len(decipheredResult)

	decryptedOut += decipheredResult + '\n'
	decryptCount += 1

		# decipheredResult,' WITH ',sowpodsItem,' AND ',
	print (decryptCount,'of ',sowpodsLength)

# Write to text file
with open('cipherresults.txt', 'w') as myfile:
	myfile.truncate()
	myfile.write(decryptedOut)
