#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	/usr/bin/python
###	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3


"""
	This Python script is written by Zhiyang Ong to sort a set of
		(key,frequency) pairs, using their keys.
	
	
	Synopsis:
	Sort a set of (key,frequency) pairs, using their keys.


	Revision History:
	December 15, 2017			Version 0.1, initial build.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'December 15, 2017'

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
from collections import namedtuple
from operator import attrgetter

###############################################################
#	Import Custom Python Modules


###############################################################
"""
	Module with method that creates a set of (key,frequency)
		pairs, and sorts these pairs using their keys.
"""
class process_key_freq_pairs:
	# =========================================================
	#	Method to create a set of (key,frequency) pairs,
	#		and sort these pairs using their keys.
	#	@return - Nothing.
	#	O(n) method, where n is the size of the set.
	@staticmethod
	def sort_pairs():
		print("	Create and manipulate set of (key,frequency) pairs.")
		# Empty set of (key,frequency) pairs, using named tuples.
		set_of_pairs = []
		# Define a (key,frequency) pair, using a named tuple.
		key_freq_pair = namedtuple("key_freq_pair", "key freq")
		# Create (key,frequency) pairs, using named tuples.
		kfp = key_freq_pair(key="Paolo", freq=23)
		# And add named tuples to the set of (key,frequency) pairs.
		set_of_pairs.append(kfp)
		kfp = key_freq_pair(key="Fosca", freq=8)
		set_of_pairs.append(kfp)
		kfp = key_freq_pair(key="Daniela", freq=39)
		set_of_pairs.append(kfp)
		kfp = key_freq_pair(key="Pippo", freq=2)
		set_of_pairs.append(kfp)
		kfp = key_freq_pair(key="Angelo", freq=51)
		set_of_pairs.append(kfp)
		kfp = key_freq_pair(key="Paola", freq=8)
		set_of_pairs.append(kfp)
		kfp = key_freq_pair(key="Caro", freq=8)
		set_of_pairs.append(kfp)
		kfp = key_freq_pair(key="Selina", freq=14)
		set_of_pairs.append(kfp)
		kfp = key_freq_pair(key="Karina", freq=71)
		set_of_pairs.append(kfp)
		kfp = key_freq_pair(key="Karyna", freq=61)
		set_of_pairs.append(kfp)
		# Enumerate each named tuple, and print its field.
		for p in set_of_pairs:
			print("Key={0}.	Frequency={1}." .format(p.key,str(p.freq))) 
		# Sort the set by key/name.
		key_sort = sorted(set_of_pairs, key=attrgetter("key"))
		print "*	*	*	*	*	*	*	*	*	*	*	*	*"
		# Enumerate and print each element in key-sorted set.
		for p in key_sort:
			print("Key={0}.	Frequency={1}." .format(p.key,str(p.freq))) 
		print "*	*	*	*	*	*	*	*	*	*	*	*	*"
		# Sort the set by key/name.
		freq_sort = sorted(set_of_pairs, key=attrgetter("freq"))
		# Enumerate and print each element in frequency-sorted set.
		for p in freq_sort:
			print("Key={0}.	Frequency={1}." .format(p.key,str(p.freq)))
		print "*	*	*	*	*	*	*	*	*	*	*	*	*"
		rev_list = reversed(freq_sort)
		# Enumerate and print each element in frequency-sorted set.
		for p in rev_list:
			print("Key={0}.	Frequency={1}." .format(p.key,str(p.freq)))
		print "*	*	*	*	*	*	*	*	*	*	*	*	*"
		# Sort the set by key/name.
		rev_key_sort = sorted(set_of_pairs, key=attrgetter("freq"), reverse = True)
		# Enumerate and print each element in frequency-sorted set.
		for p in rev_key_sort:
			print("Key={0}.	Frequency={1}." .format(p.key,str(p.freq)))
		#print "*	*	*	*	*	*	*	*	*	*	*	*	*"





