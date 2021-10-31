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

from collections import Counter

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
class keywords_analy:
	"""
		Set of common strings indicating the start of a BibTeX
			entry using a standard BibTeX entry type.
	"""
	preferred_tuple_of_BibTeX_entry_types = ("@article{", "@book{", "@booklet{", "@inbook{", "@incollection{", "@inproceedings{", "@manual{", "@mastersthesis{", "@misc{", "@phdthesis{", "@proceedings{", "@techreport{")
	tuple_of_BibTeX_entry_types = ("@article{", "@book{", "@booklet{", "@conference{", "@inbook{", "@incollection{", "@inproceedings{", "@manual{", "@mastersthesis{", "@misc{", "@phdthesis{", "@proceedings{", "@techreport{", "@unpublished")
	# ============================================================
	#	Method to collect keywords from each BibTeX entry's
	#		'Keywords' field, sort them, and display them in
	#		standard output.
	#	@param ip_f_obj - The file object for the input stream, which
	#						reads in a BibTeX file.
	#	@param ip_file - The filename of the input BibTeX file.
	#	@return nothing.
	#	O(n) method, with respect to the number of lines in the file.
	@staticmethod
	def collect_and_list_keywords(ip_f_obj,ip_file):
		"""
			A dictionary of the the number of redundant keyphrases,
				which can be found in any BibTeX entry (or publication),
				and its frequency (number of publications with this frequency).
		"""
		frequency_dict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0,25:0,26:0,27:0,28:0,29:0}
		println = "=	Reading input BibTeX file:"
		println += ip_file
		print(println)
		#op_file_obj.write(println)
		#op_file_obj.write("\n")
		# List/set of keywords found in the BibTeX database
		set_of_keywords = []
		# BibTeX key of currently enumerated BibTeX entry.
		key_of_current_bibtex_entry = "UNKNOWN"
		# Number of redundant keyphrases in the BibTeX database.
		num_redundant_keyphrases = 0
		# Number of BibTeX entries with redundant keyphrases.
		num_bibtex_entries_with_redundant_keyphrases = 0
		# Read each available line in the input BibTeX file.
		for line in ip_f_obj:
			"""
				Determine if the currently enumerated line defines the
					beginning of a BibTeX entry.
			"""
			result_is = keywords_analy.is_start_of_BibTeX_entry(line)
			if(result_is[0]):
				"""
					It does. Update placeholder of BibTeX key for currently
						processed BibTeX entry.
				"""
				key_of_current_bibtex_entry = result_is[1]
				# Remove the newline character for the BibTeX key.
				key_of_current_bibtex_entry = key_of_current_bibtex_entry.strip()
				# Remove the last character, a comma, following the BibTeX key.
				key_of_current_bibtex_entry = key_of_current_bibtex_entry[:-1]
				#print(">	",line)
				#print("<	",key_of_current_bibtex_entry)
				#print("??	",result_is[1])
			"""
				Else, do nothing.
				...
			"""
			# Number of redundant keyphrases per BibTeX entry.
			num_of_redundant_keyphrases_per_BibTeX_entry = 0
			"""
				Does this line contain the BibTeX field?
			"""
			if(keywords_analy.is_keywords_BibTeX_field(line)):
				# Yes. Remove the prefix and suffix for this line.
				keywds_line = line.replace("	Keywords = {","")
				keywds_line = keywds_line.replace("},\n","")
				# Tokenize the keywords into a list, using ", " as a delimiter.
				list_of_keywds = keywds_line.split(", ")
				"""
					Create a dictionary for keywords in this BibTeX entry
						and their frequencies.
				"""
				res = dict(Counter(i for i in list_of_keywds))
				# Sort elements in dictionary based on their frequency.
				res_lst = sorted([(v, k) for k, v in res.items()], reverse=True)
				for (freq,kwd) in res_lst:
					if 1 < freq:
						print("f:",freq," and k:",kwd,"for BibTeX key:",key_of_current_bibtex_entry,"=")
						num_redundant_keyphrases = num_redundant_keyphrases+1
						num_of_redundant_keyphrases_per_BibTeX_entry = num_of_redundant_keyphrases_per_BibTeX_entry + 1
				"""
				set_of_keywords = list(set(set_of_keywords+keywds_line))
				set_of_keywords = sorted(set_of_keywords)
				"""
			"""
				If there are redundant keyphrases for this BibTeX entry,
			"""
			if 0 < num_of_redundant_keyphrases_per_BibTeX_entry:
				# Indicate the number of redundant keyphrases.
				print("===	Number of redundant keyphrases for entry: {}." .format(num_of_redundant_keyphrases_per_BibTeX_entry))
				frequency_dict[num_of_redundant_keyphrases_per_BibTeX_entry] = frequency_dict[num_of_redundant_keyphrases_per_BibTeX_entry] + 1
				num_bibtex_entries_with_redundant_keyphrases = num_bibtex_entries_with_redundant_keyphrases + 1
		# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
		"""
		for kwd in set_of_keywords:
			#print(kwd)
			temp_kwd = kwd+"\n"
			op_file_obj.write(temp_kwd)
		"""
		# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
		"""
			Due to the following error, skip printing keywords to
				the standard output:
			"Streaming output truncated to the last 5000 lines."
		"""
		"""
		print("===	Number of keyphrases: {}" .format(len(set_of_keywords)))
		op_file_obj.write("===	Number of keyphrases: {}\n" .format(len(set_of_keywords)))
		"""
		print("===	Number of instances of redundant keyphrases: {}." .format(num_redundant_keyphrases))
		print("===	Number of BibTeX entries with redundant keyphrases: {}." .format(num_bibtex_entries_with_redundant_keyphrases))
		#op_file_obj.write("===	Number of keyphrases: {}\n" .format(num_redundant_keyphrases))
		#op_file_obj.write("\n")
		# Print the frequency distributed for the number of redundant keyphrases.
		print(frequency_dict)
	# ============================================================
	#	Method to determine if a string 'a_str' starts with the
	#		'Keywords' standard BibTeX field.
	#	@param a_str - a string to be processed.
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
	#	Method to determine if a string, which would represent the
	#		current line of the BibTeX reference database, 'a_str',
	#		is the start of a BibTeX entry using a standard BibTeX
	#		entry type.
	#	@param a_str - a string to be processed.
	#	@return a tuple (result, bibtex_key), such that
	#		result = True, if 'a_str' starts with a standard BibTeX
	#		entry type.
	#		Else, return result = False.
	#		If result = True, assign bibtex_key to the BibTeX entry
	#			for the BibTeX entry.
	#		Else, return bibtex_key = None.
	#	O(1) method.
	@staticmethod
	def is_start_of_BibTeX_entry(a_str):
		for current_bibtex_type in keywords_analy.tuple_of_BibTeX_entry_types:
			#print("~	Enumerating current_bibtex_type:::",current_bibtex_type,"=")
			if a_str.startswith(current_bibtex_type):
				current_bibtex_key = a_str.replace(current_bibtex_type,"")
				#print(".	",a_str)
				#print("..	",current_bibtex_key)
				return (True, current_bibtex_key)
			# Else, do nothing
			#print("=>	",a_str)
			#print("	::Is not the start of a BibTeX entry.")
		return (False, None)
			




















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
	#	= Start of Preprocessing.
	# Input file filename
	#ip_filename = 'references.bib'
	# If at least 1 input argument is passed to this script, ...
	if 1 < len(sys.argv):
		# Set the input file to the first input argument.
		ip_filename = sys.argv[1]
	else:
		# Else, set the default path to the BibTeX as follows.
		ip_filename = "references.bib"
	#op_filename = 'keywords.md'
	# Create a file object for reading.
	print("=	Create a file object for reading.")
	ip_file_obj = open(ip_filename, 'r')
	# Create a file object for writing.
	#print("=	Create a file object for writing.")
	#op_file_obj = open(op_filename, 'w')
	# --------------------------------------------------------
	#	= End of Preprocessing.
	print("===================================================")
	print("Displaying Sorted List of Keywords from a BibTeX Database.")
	print("")
	#"""
	#	Collect the set of all keywords found in the BibTeX database.
	#	Sort the set/list.
	#	Display the set.
	#"""
	keywords_analy.collect_and_list_keywords(ip_file_obj, ip_filename)
	# Close the file object for reading.
	print("=	Close the file object for reading.")
	#op_file_obj.write("=	Close the file object for reading.\n")
	ip_file_obj.close()
	# Get the elapsed time.
	elapsed_time = execution_time_measurement_no_ns.get_elapsed_time(mode_current_time_measurement)
	temp_text = "Elapsed time:::"+str(datetime.timedelta(seconds=elapsed_time))+"=\n"
	#op_file_obj.write(temp_text)
	# Close the file object for writing.
	#print("=	Close the file object for writing.")
	#op_file_obj.write("=	Close the file object for writing.\n")
	#op_file_obj.close()
	print("Elapsed time:::",datetime.timedelta(seconds=elapsed_time),"=")
