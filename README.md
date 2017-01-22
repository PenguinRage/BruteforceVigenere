## What is Vigenère cipher?
The Vigenère cipher is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a keyword. 
It is a simple form of polyalphabetic substitution. This cipher is not considered to being secure at all.

## Overview
This Github repository contains the code to bruteforce Vigenère cipher encrypted message to give the actual message.
Through two simple steps we compute all possible messages and then determine out of all possible calculations which is the real message.
By obtaining the actual message we can also determine the decryption key and would no longer need to bruteforce the attempt again should the encryption method be the same with the same encryption key.

## Requirements
* Python 2.7

## Example
Below is some encrypted text. Without knowing the actual encryption or decryption key we intend to find out what the message contains:
*Text can be found in cipher.txt in Github.*

```
WJHZR DIAKZ TMCYS OMLVY HISNF BNZRP
OESFJ RVLWL MIPOA LJAKD SQWLH KYSCN
RMHPB OQNQQ MNBXC CACJN BOVVT LAUWJ
RNISI FFBJO WZWIV NCWQM AUEEX TNOMR
JIIYH ISNWD Y
```

Compute permutations through my *brute_decrypt.py*

```
python brute_decryption
```

Check for Dictionary matches using a score. *For the example, 70 or above gives the top 3 matches. 80 and above gives only the correct result*

```
python detectEnglish.py <file_name> <score>
```

The higher the score reflects the accuracy towards matching words from the dictionary sowpods.txt

