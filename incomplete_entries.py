#!/usr/local/bin/python3

# Commented out IPython magic to ensure Python compatibility.
"""
	This is written by Zhiyang Ong to find BibTeX entries with
		a multi-line "Keywords" field in a BibTeX database.



	Synopsis: command name and [argument(s)]
	./incomplete_entries.py [input BibTeX file] [-h]

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
from utilities.queue_ip_arguments import queue_ip_args
# Module to perform file I/O (input/output) operations.
from utilities.file_io import file_io_operations

# Module to process input arguments to the script/program.
#from utilities.queue_ip_arguments import queue_ip_args
# Module to perform file I/O (input/output) operations.
#from utilities.file_io import file_io_operations

from timing_measurements.performance_measurement_no_ns import execution_time_measurement_no_ns


###############################################################
#	Module with methods that provides a list of BibTeX entries
#		that have a multi-line 'Keywords' field in the specified
#		BibTeX database.
class incomplete_entries:
	# List of BibTeX keys of problematic BibTeX entries.
	problematic_BibTeX_entries = []
	# ============================================================
	#	Method to find BibTeX entries with a multi-line
	#		'Keywords' field, display their BibTeX keys in the
	#		Terminal application.
	#	param ip_f_obj - The file object for the input stream, which
	#						reads in a BibTeX file.
	#	param ip_file - The filename of the input BibTeX file.
	#	@return nothing.
	#	O(n) method, with respect to the number of lines in the file.
	@staticmethod
	def find_multi_line_keywords_fields(ip_f_obj,ip_file):
		# Currently enumerated BibTeX key.
		current_bibtex_key = ""
		println = "=	Reading input BibTeX file:"
		println += ip_file
		print(println)
		# Read each available line in the input BibTeX file.
		for line in ip_f_obj:
			#print(line)
			# Is this line the 1st line of a BibTeX entry?
			if "@" == line[0]:
				current_bibtex_key = incomplete_entries.get_BibTeX_entry(line)
				#print("	Current BibTeX entry:",current_bibtex_key,"=")
			# Does this line contain the "Keywords" field?
			elif(incomplete_entries.is_keywords_BibTeX_field(line)):
				# Yes.
				#print(line)
				### Does this line not end with "},"?
				# Does this line not end with "},"?
				if not line.endswith("},"):
				#	a = 0
				#else:
					# Yes. Add current BibTeX key to the problematic list.
					incomplete_entries.problematic_BibTeX_entries.append(current_bibtex_key)
				current_bibtex_key = ""
			#else:
				# Do nothing.
				#current_bibtex_key = ""
		# Print the list of BibTeX keys of problematic BibTeX entries.
		for entry in incomplete_entries.problematic_BibTeX_entries:
			print("Problematic BibTeX key is:", entry, "=")
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
	# ============================================================
	#	Method to obtain the BibTeX key from a BibTeX entry.
	#	param a_str - a string to be processed.
	#	@return BibTeX key, if 'a_str' starts with "@", followed by
	#		a standard BibTeX entry type.
	#		Else, raise an exception.
	#	O(1) method.
	@staticmethod
	def get_BibTeX_entry(a_str):
		# Yes.
#		print "...	First line of a BibTeX entry."
		tokenized_BibTeX_entry = re.split('@|{|,',a_str)
#		for i in tokenized_BibTeX_entry:
#			print i
		# Is the type of the BibTeX entry valid?
		if (tokenized_BibTeX_entry[1] in queue_ip_args.BibTeX_entry_types):
			# Yes. Return BibTeX key.
			#return tokenized_BibTeX_entry[2].lower()
			return tokenized_BibTeX_entry[2]
		else:
			# No. Warn user that the type of BibTeX entry is invalid!
			temp_str = "Invalid type of BibTeX entry:"
			temp_str += tokenized_BibTeX_entry[1]
			print(temp_str)
			#warnings.warn("Invalid type of BibTeX entry")
			raise Exception("BibTeX entry has an invalid type!")



















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
	print("Displaying List of BibTeX Entries with Multi-line Keywords Field.")
	print("")
	# Assign input arguments to "queue_ip_args" for processing. 
	queue_ip_args.set_input_arguments(sys.argv,queue_ip_args.INCOMPLETE_ENTRIES)
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
	#ip_filename = "/Users/zhiyang/Documents/ricerca/saag-bibtex/references.bib"
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
