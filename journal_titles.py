#!/Library/Frameworks/Python.framework/Versions/Current/bin/python3
###	#!/opt/anaconda3/bin/python

###	#!/Users/zhiyang/anaconda3/bin/python

#	#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	/usr/bin/python
###	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	#!/usr/bin/python -mtimeit

"""
	This is written by Zhiyang Ong to display a set of journal titles
		from BibTeX entries in a BibTeX database.



	Synopsis: command name and [argument(s)]
	./journal_titles.py [input BibTeX file] [-h]

	Parameters:
	[input BibTeX file]:	A BibTeX database.

	[-h]				:	If an optional "-h" flag is used as an
							input argument, show the brief user manual
							and exit (terminate the program).


	Its procedure is described as follows:
	Initialize an empty list of journal titles.
	Enumerate each line in the input BibTeX database.
		If the currently enumerated line contains the 'Journal'
			BibTeX field,
			Add its contents to set of journal titles. 
	Sort the set of journal titles.

	Notes/Assumptions:
	Assume that the 'Journal' standard BibTeX field is a single line
		field.


	Revision History:
	April 17, 2017			Version 0.1, initial build.
"""

#	The MIT License (MIT)

#	Copyright (c) <2014-2017> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?

#	==========================================================

__author__ = 'Zhiyang Ong'
__version__ = '0.2'
__date__ = 'Apr 17, 2017'

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
	filecmp		For file comparison. 
"""

import sys
import os
import os.path
from subprocess import call
import time
import warnings
import re
import filecmp

###############################################################

#	Import Custom Python Modules

# Module to process input arguments to the script/program.
from utilities.queue_ip_arguments import queue_ip_args
# Module to perform file I/O (input/output) operations.
from utilities.file_io import file_io_operations


###############################################################
#	Module with methods that collects the set of journal titles
#		found in all the 'Journal' fields in this BibTeX database.
class journals_show:
	# ============================================================
	#	Method to collect journal titles from each BibTeX entry's
	#		'Journal' field, sort them, and display them in
	#		standard output.
	#	@param ip_f_obj - The file object for the input stream, which
	#						reads in a BibTeX file.
	#	@param ip_file - The filename of the input BibTeX file.
	#	@return nothing.
	#	O(n) method, with respect to the number of lines in the file.
	@staticmethod
	def collect_and_list_journals(ip_f_obj,ip_file):
		println = "=	Reading input BibTeX file:"
		println += ip_file
		print(println)
		# List/set of journal titles found in the BibTeX database
		set_of_journal_titles = []
		# Read each available line in the input BibTeX file.
		for line in ip_f_obj:
			if(journals_show.is_journal_BibTeX_field(line)):
				journal_line = line.replace("	Journal = {","")
				journal_line = journal_line.replace("},\n","")
				#journal_line = journal_line.split(", ")
				journal_line = journal_line.split("~")
				set_of_journal_titles = list(set(set_of_journal_titles+journal_line))
				set_of_journal_titles = sorted(set_of_journal_titles)
		for kwd in set_of_journal_titles:
			print(kwd)
		print("===	Number of journal titles: {}" .format(len(set_of_journal_titles)))

	# ============================================================
	#	Method to determine if a string 'a_str' starts with the
	#		'Journal' standard BibTeX field.
	#	@param a_str - a string to be processed.
	#	@return True, if 'a_str' starts with the 'Journal'
	#		standard BibTeX field.
	#		Else, return False.
	#	O(1) method.
	@staticmethod
	def is_journal_BibTeX_field(a_str):
		if(a_str.startswith("	Journal = {")):
			return True
		else:
			return False



















###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	# --------------------------------------------------------
	#	= Start of Preprocessing.
	queue_ip_args.preprocessing()
	# --------------------------------------------------------
	#	= End of Preprocessing.
	print("===================================================")
	print("Displaying Sorted List of Journal Titles from a BibTeX Database.")
	print("")
	# Assign input arguments to "queue_ip_args" for processing. 
	queue_ip_args.set_input_arguments(sys.argv,queue_ip_args.GET_JOURNAL)
	# Check if user wants to read the brief user manual.
	queue_ip_args.check_if_help_wanted()
	# Process the first input argument.
	print("=	Process the first input argument.") 
	ip_filename = queue_ip_args.process_1st_ip_arg()
	# Create a file object for reading.
	print("=	Create a file object for reading.")
	ip_file_obj = file_io_operations.open_file_object_read(ip_filename)
	"""
		Collect the set of all journal titles found in the BibTeX
			database.
		Sort the set/list.
		Display the set.
	"""
	journals_show.collect_and_list_journals(ip_file_obj, ip_filename)
	# Close the file object for reading.
	print("=	Close the file object for reading.")
	file_io_operations.close_file_object(ip_file_obj)
