#!/usr/local/bin/python3

# Commented out IPython magic to ensure Python compatibility.
"""
	This is written by Zhiyang Ong to display a set of keywords from
		BibTeX entries in a BibTeX database.



	Synopsis: command name and [argument(s)]
	./keywords_display.py [input BibTeX file] [-h]

	Parameters:
	[input BibTeX file]:	A BibTeX database.

	[-h]:					If an optional "-h" flag is used as an
							input argument, show the brief user manual
							and exit (terminate the program).


	Its procedure is described as follows:
	Initialize an empty list of keywords.
	Enumerate each line in the input BibTeX database.
		If the currently enumerated line contains the 'Keywords'
			BibTeX field,
			Add its contents to set of keywords. 
	Sort the set of keywords.

	Notes/Assumptions:
	Assume that the 'Keywords' standard BibTeX field is a single line
		field.
	Assume that each pair of keywords, or keyphrases, is separated 


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
	datetime	For operations regarding date and time.
"""

import sys
import os
import os.path
from subprocess import call
import time
import warnings
import re
import filecmp
import datetime

###############################################################

#	Import Custom Python Modules

# Module to process input arguments to the script/program.
#from utilities.queue_ip_arguments import queue_ip_args
# Module to perform file I/O (input/output) operations.
#from utilities.file_io import file_io_operations

from timing_measurements.performance_measurement_no_ns import execution_time_measurement_no_ns


###############################################################
#	Module with methods that collects the set of keywords found
#		in all the 'Keywords' fields in this BibTeX database.
class incomplete_entries:
	list_of_keywords = []
	# ============================================================
	#	Method to collect keywords from each BibTeX entry's
	#		'Keywords' field, sort them, and display them in
	#		standard output.
	#	param ip_f_obj - The file object for the input stream, which
	#						reads in a BibTeX file.
	#	param ip_file - The filename of the input BibTeX file.
	#	@return nothing.
	#	O(n) method, with respect to the number of lines in the file.
	@staticmethod
	def find_multi_line_keywords_fields(ip_f_obj,ip_file):
		println = "=	Reading input BibTeX file:"
		println += ip_file
		print(println)
		op_file_obj.write(println)
		op_file_obj.write("\n")
		# List/set of keywords found in the BibTeX database
		set_of_keywords = []
		# Read each available line in the input BibTeX file.
		for line in ip_f_obj:
			if(incomplete_entries.is_keywords_BibTeX_field(line)):
				keywds_line = line.replace("	Keywords = {","")
				keywds_line = keywds_line.replace("},\n","")
				keywds_line = keywds_line.split(", ")
				set_of_keywords = list(set(set_of_keywords+keywds_line))
		"""
			By shifting the following statement to sort keyphrases per
				iteration (in the "if" statement) to outside the
				"for" loop, I noticed a performance speedup from
				13:36.270975 (minutes:seconds) to 1:42.645526 (minutes:seconds).

			(13*60+36)/(60+42) = (13*60+36)/102 = 8.

			Hence, it is a 8X (or 8 times) speedup in performance.

			To empirically determine this for multiple run-time conditions,
				since I use this script when using different combinations
				of software applications, I would repeat the experiment
				multiple times (>= 5, such as 10 times), find their
				arithmetic average/mean, and the relative difference
				between their arithmetic average/mean.

			If the set of keyphrases is not sorted, the output list of
				keyphrases would not be sorted and difficult to use
				effectively.
				That is, it is hard to use an unsorted list to check
					if a keyphrase exists in this set and look for
					similar keyphrases.
		"""
		set_of_keywords = sorted(set_of_keywords)
		for kwd in set_of_keywords:
			#print(kwd)
			temp_kwd = kwd+"\n"
			#op_file_obj.write(temp_kwd)
			if 60 < len(kwd):
				# Add beginning and end markers to help distinguish long keyphrases.
				op_file_obj.write("=start\n")
				op_file_obj.write(temp_kwd)
				op_file_obj.write("=end\n")
			else:
				op_file_obj.write(temp_kwd)
		"""
			Due to the following error, skip printing keywords to
				the standard output:
			"Streaming output truncated to the last 5000 lines."
		"""
		print("===	Number of keyphrases: {}" .format(len(set_of_keywords)))
		op_file_obj.write("===	Number of keyphrases: {}\n" .format(len(set_of_keywords)))
		#op_file_obj.write("\n")
	# ============================================================
	#	Method to determine if a string 'a_str' starts with the
	#		'Keywords' standard BibTeX field.
	#	param a_str - a string to be processed.
	#	@return True, if 'a_str' starts with the 'Keywords'
	#		standard BibTeX field.
	#		Else, return False.
	#	O(1) method.
	@staticmethod
	def is_keywords_BibTeX_field(a_str):
		if(a_str.startswith("	Keywords = {")):
			return True
		else:
			return False



















###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	# --------------------------------------------------------
	#	= Set up loading of BibTeX database
	# Code to read csv file into Colaboratory:
	# Type of current time measurement.
	mode_current_time_measurement = "perf_counter"
	# Set the initial timestamp.
	execution_time_measurement_no_ns.set_initial_timestamp()
	# --------------------------------------------------------
	#	= Start of Preprocessing.
	queue_ip_args.preprocessing()
	# --------------------------------------------------------
	#	= End of Preprocessing.
	print("===================================================")
	print("Displaying Sorted List of publishers from a BibTeX Database.")
	print("")
	# Assign input arguments to "queue_ip_args" for processing. 
	queue_ip_args.set_input_arguments(sys.argv,queue_ip_args.KEYWORDS_DISPLAY)
	# Check if user wants to read the brief user manual.
	queue_ip_args.check_if_help_wanted()
	# Process the first input argument.
	print("=	Process the first input argument.")
	ip_filename = queue_ip_args.process_1st_ip_arg()
	# Create a file object for reading.
	print("=	Create a file object for reading.")
	ip_file_obj = file_io_operations.open_file_object_read(ip_filename)
	# --------------------------------------------------------
	#	Default values for input BibTeX database for processing.
	ip_filename = "/Users/zhiyang/Documents/ricerca/saag-bibtex/references.bib"
	#	No output files needed.
	#op_filename = 'keywords.md'
	# Create a file object for reading.
	"""
	print("=	Create a file object for reading.")
	ip_file_obj = open(ip_filename, 'r')
	"""
	# Create a file object for writing.
	"""
	print("=	Create a file object for writing.")
	op_file_obj = open(op_filename, 'w')
	"""
	# --------------------------------------------------------
	#	= End of Preprocessing.
	print("===================================================")
	print("Find multi-line Keywords field from a BibTeX Database.")
	print("")
	#"""
	#	Find BibTeX entries with multi-line Keywords field in the
	#		BibTeX database.
	#	Display the list.
	#"""
	incomplete_entries.find_multi_line_keywords_fields(ip_file_obj, ip_filename)
	# Close the file object for reading.
	print("=	Close the file object for reading.")
	ip_file_obj.close()
	# Get the elapsed time.
	elapsed_time = execution_time_measurement_no_ns.get_elapsed_time(mode_current_time_measurement)
	temp_text = "Elapsed time:::"+str(datetime.timedelta(seconds=elapsed_time))+"=\n"
	print("Elapsed time:::",datetime.timedelta(seconds=elapsed_time),"=")
