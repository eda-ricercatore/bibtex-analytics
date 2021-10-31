#!/usr/local/bin/python3

"""
	This Python script is written by Zhiyang Ong to test the
		module to calculate the factorial of a number.

	The results for this script are compared to the table of
		factorials in \cite{Pierce2019a}, and validated/verified
		for factorials from 0.
	 

	Synopsis:
	Test module that calculates the factorial of a number.



	Notes/Assumptions:
	+ Only the factorials of non-negative integers can be computed.
	+ If the input to the iterative or recursive factorial function
		is a negative number, not an integer (e.g., floating-point
		number), not a number (e.g., a string), return the "None"
		object for the method caller to process.
		- This avoids having to raise exceptions when users try
			to determine the factorial of anything that is not a
			non-negative integer.
		- See references on exception safety \cite{Abrahams1998,Abrahams2001,WikipediaContributors2016f} \cite[Subsection 4.4 on ``Writing exception safe code'']{WikibooksContributors2016}.


	Revision History:
	September 6, 2019			Version 0.1	Script.

	References:
		[Pierce2019a]
			Rod Pierce, "Factorial Function," from Maths Is Fun, 2019. Available online from "Maths Is Fun: Numbers" at: https://www.mathsisfun.com/numbers/factorial.html; September 19, 2019 is the last access date.
				[No address]
				https://www.mathsisfun.com/citation.php
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'September 6, 2019'

#	The MIT License (MIT)

#	Copyright (c) <2019> <Zhiyang Ong>

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

	pathlib->Path
				For mapping a string to a path.
	datetime	To obtain information about the current date and time.
	time	To obtain information about the current time.
	warnings	Provide warnings to users without terminating the
					program abruptly.
"""

import sys
import os
import os.path
#from pathlib import Path
from subprocess import call
import time
import warnings
import re
import datetime
import time
import warnings

###############################################################
#	Import Custom Python Modules

# Package and module that compute the factorial of a number.
from utilities.timing_measurements.get_factorial import calculate_factorial



###############################################################
"""
	Module that tests methods that determine the factorial of
		a number.
"""
class calculate_factorial_tester:
	# ============================================================
	##	Method to test the method to calculate the factorial of
	#		a number by iteration.
	#	@param - None.
	#	@return - Nothing.
	#	O(n!) method, because it calls functions that calculate
	#		the factorial of numbers, which is O(n!).
	@staticmethod
	def test_get_factorial_iteration():
		print("= Testing calculate_factorial.get_factorial_recursion() method.")
		print("	... Test: get_factorial_iteration(4)			{}.")
		statistical_analysis.increment_number_test_cases_used()
		if 24 == calculate_factorial.get_factorial_iteration(4):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		# ValueError: invalid literal for int() with base 10: 'my string'
		print("get_factorial_iteration('my string'):",calculate_factorial.get_factorial_iteration("my string"),"=")
		print("get_factorial_iteration(125.23429):",calculate_factorial.get_factorial_iteration(125.23429),"=")
		print("get_factorial_iteration(None):",calculate_factorial.get_factorial_iteration(None),"=")
		print("get_factorial_iteration(-345):",calculate_factorial.get_factorial_iteration(-345),"=")
	# ============================================================
	##	Method to test the method to calculate the factorial of
	#		a number by recursion.
	#	@param - None.
	#	@return - Nothing.
	#	O(n!) method, because it calls functions that calculate
	#		the factorial of numbers, which is O(n!).
	@staticmethod
	def test_get_factorial_recursion():
		print("=	Test the factorial computation method using recursion.")
		print("get_factorial_recursion(4):",calculate_factorial.get_factorial_recursion(4),"=")
		# ValueError: invalid literal for int() with base 10: 'my string'
		print("get_factorial_recursion('my string'):",calculate_factorial.get_factorial_recursion("my string"),"=")
		print("get_factorial_recursion(125.23429):",calculate_factorial.get_factorial_recursion(125.23429),"=")
		print("get_factorial_recursion(None):",calculate_factorial.get_factorial_recursion(None),"=")
		print("get_factorial_recursion(-345):",calculate_factorial.get_factorial_recursion(-345),"=")
	# =========================================================
	#	Method to test methods that determine the factorial of a
	#		number.
	#	@param - None.
	#	@return - Nothing.
	#	O(n!) method, because it calls functions that calculate
	#		the factorial of numbers, which is O(n!).
	@staticmethod
	def test_get_factorial_methods():
		print("")
		print("")
		print("==	Testing class: calculate_factorial.")
		print("==================================================")
		calculate_factorial_tester.test_get_factorial_iteration()
		"""
			Add whitespace before testing the factorial computation
				method using recursion.
		"""
		print("\n\n")
		calculate_factorial_tester.test_get_factorial_recursion()
