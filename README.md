Simple One Time Pad Breaker
===============================

Quick and dirty script to test strings against the One Time Pad cipher. Assumes two encrypted messages (Cipher 1 + 2) created with a one time pad cipher are encrypted with the same key and performs the following operation:

	- Uses a test string, inputted with common English words (eg. " and ") to derive the key at every position in Cipher 1
	- Runs key against matching position in Cipher 2
	- Runs regex against decrypted Message 2 to filter out everything but alphabetic characters and common punctuation. Prints other possible decrypted message parts.

Created for the Udacity Applied Cryptography course Challenge 1.

Included files
==============

* challenge1.py: Main file. Run this against test strings
* provided.py: Provided functions
* helper.py: Helper functions (XOR function)