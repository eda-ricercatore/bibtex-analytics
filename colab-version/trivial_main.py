#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	/usr/bin/python
###	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	#!/usr/bin/python -mtimeit


"""
	This Python script is written by Zhiyang Ong to learn how to
		import a Python package and module in Google Colab, via
		a Jupyter notebook.

	References:
	https://colab.research.google.com/notebooks/snippets/importing_libraries.ipynb

	Revision History:
	November 1, 2019			Version 0.1, initial build.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'November 1, 2019'

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
"""

"""
import sys
import os
import os.path
#from pathlib import Path
from subprocess import call
import time
import warnings
import re
"""


###############################################################
#	Import Custom Python Modules

# Module to test if I can import a Python package and module.
from utilities.simple_module import simple





###############################################################
#	Module with methods that clean BibTeX files.
class Try_to_Import_Package:
	"""
		Number of times that the "Hello World" print function
			has been called.
	"""
	number_times_executed = 0
	# =========================================================
	#	Accessor and Mutator method.
	# =========================================================
	#	Method to print the number of times that the
	#		"Hello World" print function has been called, and
	#		increment this number by one.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def get_number_times_executed():
		Try_to_Import_Package.number_times_executed = Try_to_Import_Package.number_times_executed + 1
		print("	Try_to_Import_Package 'Hello World' function called:",Try_to_Import_Package.number_times_executed,"times.")









###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	for x in range(10):
		simple.get_number_times_executed()
		Try_to_Import_Package.get_number_times_executed()
	
