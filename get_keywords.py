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
class keywords_show:
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
	def collect_and_list_keywords(ip_f_obj,ip_file):
		println = "=	Reading input BibTeX file:"
		println += ip_file
		print(println)
		op_file_obj.write(println)
		op_file_obj.write("\n")
		# List/set of keywords found in the BibTeX database
		set_of_keywords = []
		# Read each available line in the input BibTeX file.
		for line in ip_f_obj:
			if(keywords_show.is_keywords_BibTeX_field(line)):
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
	#	= Start of Preprocessing.
	# Input file filename
	#ip_filename = 'references-june-24-2020-0150.bib'
	#ip_filename = 'references-june-26-2020-0033.bib'
	#ip_filename = 'references-june-26-2020-0145.bib'
	#ip_filename = 'references-june-26-2020-0217.bib'
	#ip_filename = 'references-july-20-2020-1917.bib'
	#ip_filename = 'references-august-23-2020-2315.bib'
	#ip_filename = 'references-august-21-2020-1021.bib'
	#ip_filename = 'references-september-3-2020-0754.bib'
	#ip_filename = 'references-september-10-2020-2021.bib'
	#ip_filename = 'references-september-11-2020-1553.bib'
	#ip_filename = 'references-october-1-2020-1520.bib'
	#ip_filename = 'references-october-7-2020-1334.bib'
	#ip_filename = 'references-november-2-1408.bib'
	#ip_filename = 'references-november-20-2020-1707.bib'
	#ip_filename = 'references-december-21-2020-2032.bib'
	#ip_filename = 'references-february-9-2020-1115.bib'
	#ip_filename = "references-april-9-2021-0810.bib"
	#ip_filename = "references-may-5-2021-1448.bib"
	#ip_filename = "references-may-15-2021-2154.bib"
	#ip_filename = "references-may-21-2021-2004.bib"
	#ip_filename = "references-may-29-2021-1126.bib"
	#ip_filename = "references-may-29-2021-1253.bib"
	#ip_filename = "references-may-30-2021-2306.bib"
	#ip_filename = "references-june-11-2021-2016.bib"
	#ip_filename = "references-july-6-2021-1839.bib"
	#ip_filename = "references-august-15-2021-2321.bib"
	#ip_filename = "references-august-21-2021-1735.bib"
	#ip_filename = "references-september-2-2021-1531.bib"
	#ip_filename = "references-september-3-2021-0320.bib"
	#ip_filename = "references-september-17-2021-1142.bib"
	#ip_filename = "references-september-27-2021-1307.bib"
	#ip_filename = "references-october-4-2021-1249.bib"
	#ip_filename = "references-october-26-2021-2151.bib"
	#ip_filename = "references-november-2-2021-2059.bib"
	#ip_filename = "references-november-4-2021-1252.bib"
	#ip_filename = "references-november-4-2021-1456.bib"
	#ip_filename = "references-november-17-2021-2334.bib"
	#ip_filename = "references-november-29-2021-1242.bib"
	#ip_filename = "references-december-2-2021-0046.bib"
	#ip_filename = "references-december-8-2021-1056.bib"
	#ip_filename = "references-december-10-2021-1300.bib"
	#ip_filename = "references-december-13-2021-1521.bib"
	#ip_filename = "references-december-20-2021-1558.bib"
	#ip_filename = "references-december-21-2021-1933.bib"
	#ip_filename = "references-january-4-2022-2304.bib"
	#ip_filename = "references-january-13-2022-0945.bib"
	#ip_filename = "references-january-13-2022-1532.bib"
	#ip_filename = "references-january-15-2022-1916.bib"
	#ip_filename = "references-january-18-2022-1759.bib"
	#ip_filename = "references-january-22-2022-0955.bib"
	#ip_filename = "references-january-27-2022-1530.bib"
	#ip_filename = "references-february-2-2022-1547.bib"
	#ip_filename = "references-february-12-2022-1719.bib"
	#ip_filename = "references-february-18-2022-1357.bib"
	#ip_filename = "references-february-22-2022-2032.bib"
	#ip_filename = "references-february-23-2021-1304.bib"
	#ip_filename = "references-march-9-2022-1457.bib"
	#ip_filename = "references-march-10-2022-1728.bib"
	#ip_filename = "references-march-22-2022-1123.bib"
	#ip_filename = "references-march-30-2022-1451.bib"
	#ip_filename = "references-april-3-2022-1736.bib"
	#ip_filename = "references-april-4-2022-1018.bib"
	#ip_filename = "references-april-10-2022-1636.bib"
	#ip_filename = "references-april-12-2022-1515.bib"
	#ip_filename = "references-april-13-2022-1608.bib"
	#ip_filename = "references-april-13-2022-1700.bib"
	#ip_filename = "references-april-14-2022-1116.bib"
	#ip_filename = "references-april-14-2022-1256.bib"
	#ip_filename = "references-april-14-2022-1551.bib"
	#ip_filename = "references-april-15-2022-1832.bib"
	#ip_filename = "references-april-17-2022-2351.bib"
	#ip_filename = "references-april-19-2022-1345.bib"
	#ip_filename = "references-april-19-2022-2013.bib"
	#ip_filename = "references-april-27-2022-1244.bib"
	#ip_filename = "references-may-6-2022-1332.bib"
	#ip_filename = "references-may-7-2022-2343.bib"
	#ip_filename = "references-may-9-2022-1222.bib"
	#ip_filename = "references-may-9-2022-1339.bib"
	#ip_filename = "references-may-9-2022-1707.bib"
	#ip_filename = "references-may-10-2022-0225.bib"
	#ip_filename = "references-may-14-2022-1718.bib"
	#ip_filename = "references-may-14-2022-1743.bib"
	ip_filename = "references-may-17-2022-1827.bib"
	op_filename = 'keywords.md'
	# Create a file object for reading.
	print("=	Create a file object for reading.")
	ip_file_obj = open(ip_filename, 'r')
	# Create a file object for writing.
	print("=	Create a file object for writing.")
	op_file_obj = open(op_filename, 'w')
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
	keywords_show.collect_and_list_keywords(ip_file_obj, ip_filename)
	# Close the file object for reading.
	print("=	Close the file object for reading.")
	op_file_obj.write("=	Close the file object for reading.\n")
	ip_file_obj.close()
	# Get the elapsed time.
	elapsed_time = execution_time_measurement_no_ns.get_elapsed_time(mode_current_time_measurement)
	temp_text = "Elapsed time:::"+str(datetime.timedelta(seconds=elapsed_time))+"=\n"
	op_file_obj.write(temp_text)
	# Close the file object for writing.
	print("=	Close the file object for writing.")
	op_file_obj.write("=	Close the file object for writing.\n")
	op_file_obj.close()
	print("Elapsed time:::",datetime.timedelta(seconds=elapsed_time),"=")
