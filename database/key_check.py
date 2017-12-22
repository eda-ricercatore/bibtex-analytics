#!/usr/bin/python
###	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3


"""
	This Python script is written by Zhiyang Ong to determine if a
		BibTeX key is valid.
	
	
	Synopsis:
	Check the validity of a BibTeX key.


	Revision History:
	December 19, 2017			Version 0.1, initial build.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'December 19, 2017'

#	The MIT License (MIT)

#	Copyright (c) <2014-2017> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?

###############################################################
"""
	Import modules from The Python Standard Library.
	sys			Get access to any command-line arguments.
	os			Use any operating system dependent functionality.
	os.path		For pathname manipulations.
	
	subprocess -> call
				To make system calls.

	time		To measure elapsed time.
	warnings	Raise warnings.
	re			Use regular expressions.

	collections -> namedtuple
				To use named tuples.
	operator -> attrgetter
				To manipulate attributes of a named tuple as callable
					objects.
"""

#import sys
#import os
#import os.path
#from subprocess import call
#import time
import warnings
#import re
#from collections import namedtuple
#from operator import attrgetter

###############################################################
#	Import Custom Python Modules


###############################################################
"""
	Module with methods that check the validity of a BibTeX key.

	Support for class instantiation is not provided, to avoid
		acquiring a collection of useless "check_bibtex_key"
		objects.

	Check if all methods return a boolean TRUE to indicate that
		all the conditions required for a valid BibTeX key are
		TRUE, or indicate the condition(s) that cause the BibTeX
		key to be invalid.

	Check if none of the characters in the string are whitespace
		characters; that is, check that the string has no white
		space.

	Check if all the characters in the string are alphanumeric
		characters; there are no special characters in the string.
"""  
class check_bibtex_key:
	# =========================================================
	#	Method to check the validity of a BibTeX key.
	#	@param str - A string containing the BibTeX key.
	#	@return a boolean TRUE if the BibTeX key is valid.
	#		Else, return FALSE.
	#	O(n) method, where n is the number of characters of the key.
	@staticmethod
	def is_bibtex_key_valid(str):
		if has_no_whitespace(str) and has_only_alphanumeric_characters(str):
			return True
		else:
			return False
	# =========================================================
	#	Method to check if the BibTeX key has white space.
	#	@return - Nothing.
	#	@return a boolean TRUE if the BibTeX key has no white space.
	#		Else, return FALSE.
	#	O(n) method, where n is the number of characters of the key.
	@staticmethod
	def has_no_whitespace(str):
		if False:
			return True
		else:
			return False
	# =========================================================
	#	Method to check if the BibTeX key has only alphanumeric
	#		characters.
	#	@return - Nothing.
	#	O(n) method, where n is the number of characters of the key.
	@staticmethod
	def has_only_alphanumeric_characters(str):
		return str.isalnum()
	# =========================================================
	#	Method to tokenize the first line of each BibTeX entry, 
	#		which contains a unique BibTeX key.
	#	@return a tokenized string representing the BibTeX key.
	#	O(n) method, where n is the character length of the string.
	@staticmethod
	def tokenization_entry_key(str):
		tokenized_BibTeX_entry = re.split('@|{|,',line)
		return "Hello World!"



"""
	Do I provide a function to tokenize each line the same way?
	I have tokenized the following BibTeX fields differently.
	*	BibTeX key
	*	Keywords
	*	Publisher
	*	Series
	
	Yes.
"""





