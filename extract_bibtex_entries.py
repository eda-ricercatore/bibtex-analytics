#!/Users/zhiyang/anaconda3/bin/python

#	#!/usr/local/bin/python3


"""
	This is written by Zhiyang Ong to extract a subset of BibTeX entries
		from a BibTeX database, using a non-empty subset of the following:
	+ a set of BibTeX keys
	+ a set of keyphrases, stored as optional metadata for each BibTeX entry



	Synopsis: command name and [argument(s)]
	./extract_bibtex_entries.py [-h] [-k] [set of BibTeX keys stored as a CSV file] [-m] [set of keyphrases stored as a CSV file]
	./extract_bibtex_entries.py [-h] [-k] [set of BibTeX keys stored as a CSV file]
	./extract_bibtex_entries.py [-h] [-m] [set of keyphrases stored as a CSV file]
	./extract_bibtex_entries.py [-h] [-k] [set of BibTeX keys stored as a CSV file] [-m] [set of keyphrases stored as a CSV file]
	./extract_bibtex_entries.py [-k] [set of BibTeX keys stored as a CSV file] [-m] [set of keyphrases stored as a CSV file] [-h]
	./extract_bibtex_entries.py [-k] [set of BibTeX keys stored as a CSV file] [-h] [-m] [set of keyphrases stored as a CSV file]
	./extract_bibtex_entries.py [-k] [-m] [set of keyphrases stored as a CSV file] [-k] [set of BibTeX keys stored as a CSV file]
	./extract_bibtex_entries.py [-h]
	./extract_bibtex_entries.py [-k] [set of BibTeX keys stored as a CSV file] [-m] [set of keyphrases stored as a CSV file]
	./extract_bibtex_entries.py [-k] [set of BibTeX keys stored as a CSV file]
	./extract_bibtex_entries.py [-m] [set of keyphrases stored as a CSV file]
	./extract_bibtex_entries.py [-m] [set of keyphrases stored as a CSV file] [-k] [set of BibTeX keys stored as a CSV file]
	./extract_bibtex_entries.py [-h] [-k] [set of BibTeX keys stored as a CSV file] [-m] [set of keyphrases stored as a CSV file] [-a] [names of authors as a string] [-z] [names of authors as a string] [-b] [booktitle as a string] [-j] [journal title as a string] [-s] [book series as a string] [-u] [name of university as a string]


	Parameters:
	[input BibTeX file]:	A BibTeX database.

	[-h]:					If an optional "-h" flag is used as an
								input argument, show the brief user manual
								and exit (terminate the program).

	[-k]:					If an optional "-k" flag is used as an
								input argument, process the CSV file for
								the set of BibTeX keys that I would use
								to extract BibTeX entries.

	[-m]:					If an optional "-m" flag is used as an
							input argument, process the CSV file for
								the set of keyphrases that I would use
								to extract BibTeX entries.

	[-a]:					If an optional "-a" flag is used as an
							input argument, accept the following string
								as the name of the author(s) to search
								for in the BibTeX database.
								This is used to extract a subset of
									BibTeX entries that match this name
									(or these names).
								For names that have spaces in them, use
									double quotes to enclose them.
								The match has to be exact.

	[-z]:					If an optional "-z" flag is used as an
							input argument, accept the following string
								as the name of the author(s) to search
								for in the BibTeX database.
								This is used to extract a subset of
									BibTeX entries that contain this name
									(or these names) as a subset of names.
								Delimit the 'Author' field with " and "
									and check if the author or any co-author
									has this exact name match, for the
									last name (or surname).


	[-b]:					If an optional "-b" flag is used as an
							input argument, accept the following string
								as the booktitle to search for in the
								BibTeX database.
								This is used to extract a subset of
									BibTeX entries that match this
									booktitle.
								For booktitles that have spaces in them,
									use double quotes to enclose them.

	[-j]:					If an optional "-j" flag is used as an
							input argument, accept the following string
								as the title of the journal to search
								for in the BibTeX database.
								This is used to extract a subset of
									BibTeX entries that match this
									journal title.
								For journal titles that have spaces in them,
									use double quotes to enclose them.

	[-s]:					If an optional "-s" flag is used as an
							input argument, accept the following string
								as the series of books to search for
								in the BibTeX database.
								This is used to extract a subset of
									BibTeX entries that match this series.
								For series titles that have spaces in them,
									use double quotes to enclose them.

	[-u]:					If an optional "-u" flag is used as an
							input argument, accept the following string
								as the school to search for in the
								BibTeX database.
								This is used to extract a subset of
									BibTeX entries that match this
									university.
								For university names that have spaces
									in them, use double quotes to enclose them.




	Its procedure is described as follows:
	
	Process input arguments.
	If the [-h] input argument/option is selected,
		print the help manual with the synopsis of the command name
		and argument(s).
		This input argument does not have to end/stop the program
			immediately.
	Open an input file object for the BibTeX database.
	Parse the BibTeX database, via a BibTeX parser and the file object.
	Open an input file object for the CSV input file(s).
	Parse the CSV file, via CSV import, pandas, and the file object.
	Enumerate each BibTeX entry in the input BibTeX database.
		If the [-k] input argument/option is selected,
			find the set of records (of BibTeX entries) that
			have BibTeX keys found in the set of BibTeX keys,
			and print out information about these records into
			an output file.
		If the [-m] input argument/option is selected,
			find the set of records (of BibTeX entries) that
			have keyphrases found in the set of keyphrases,
			and print out information about these records into
			an output file.
		If the [-a] input argument/option is selected,
			find the set of records (of BibTeX entries) that
			have include the following substring in the author field,
			and print out information about these records into
			an output file.
			Matches have to be exact.
		If the [-z] input argument/option is selected,
			find the set of records (of BibTeX entries) that
			have include the following substring in a subset of the
			author field, and print out information about these records
			into an output file.
			Delimit the 'Author' field by " and ", and check if the name
				of the author or any co-author matches this string for
				the last name (or surname).
				Matches have to be exact.
				Ignore matches for full name or first/given name, since
					many authors ignore their middle name(s), and may
					also only indicate their first name initial in certain
					publications but full name otherwise.
		If the [-b] input argument/option is selected,
			find the set of records (of BibTeX entries) that
			have include the following substring in the 'Booktitle' field,
			and print out information about these records into
			an output file.
		If the [-j] input argument/option is selected,
			find the set of records (of BibTeX entries) that
			have include the following substring in the 'Journal' field,
			and print out information about these records into
			an output file.
		If the [-s] input argument/option is selected,
			find the set of records (of BibTeX entries) that
			have include the following substring in the 'Series' field,
			and print out information about these records into
			an output file.
		If the [-u] input argument/option is selected,
			find the set of records (of BibTeX entries) that
			have include the following substring in the 'School' field,
			and print out information about these records into
			an output file.
		If no input argument/option is selected, print the help manual.

		



	Notes/Assumptions:
	Assume that the 'Keywords' standard BibTeX field is a single line
		field.
	Assume that each pair of keywords, or keyphrases, is separated by
		", " in the 'Keywords' fields of the BibTeX database, and by
		"," in the CSV file.
	CSV refers to comma-separated values, and is a delimited text file
		that uses commas (or ",") to separate/delimit values.

	Since the installation of packages via PyPI are placed in the Anaconda
		"Conda" environment, and my Python environment is dependent on the
		"Conda" package and environment management system, I have to use
		the Python interpreter from Conda to use the PyPI package installations.
	Else, I can use other Python interpreters, one of which is commented out
		to enable the usage of the Python interpreter from Conda.
	If the -h option is used, print the "help" information that includes
		a synopsis of the command name (name of this Python script) and
		list of optional input arguments.
	For other options, they must come in pairs, and cannot be separated
		by other options. 
		They have either of the following formats:
	+ ./extract_bibtex_entries.py [-h]
	+ ./extract_bibtex_entries.py [option flag] [filename]
	+ ./extract_bibtex_entries.py [-h] [option flag] [filename]
	+ ./extract_bibtex_entries.py [option flag] [filename] [-h]
	+ ./extract_bibtex_entries.py [-h] [option flag] [string]
	+ ./extract_bibtex_entries.py [option flag] [string]
	+ ./extract_bibtex_entries.py [option flag] [string] [-h]
	+ ./extract_bibtex_entries.py [option flag] [filename] [option flag] [string]
	+ ./extract_bibtex_entries.py [-h] [option flag] [filename] [option flag] [string]
	+ ./extract_bibtex_entries.py [option flag] [filename] [option flag] [string] [-h]
	+ ./extract_bibtex_entries.py [option flag] [filename] [-h] [option flag] [string]
	+ ./extract_bibtex_entries.py [option flag] [string] [option flag] [filename]
	+ ./extract_bibtex_entries.py [-h] [option flag] [string] [option flag] [filename]
	+ ./extract_bibtex_entries.py [option flag] [string] [option flag] [filename] [-h]
	+ ./extract_bibtex_entries.py [option flag] [string] [-h] [option flag] [filename]
	+ ./extract_bibtex_entries.py 

	Assume that manual input is error prone, set the name/path of the
		output file in the introductory section (or preamble) that can
		be modified by others.
		This avoids having users specify the name/path of the output
			file as an input argument.




	Requirements:
	+ Installation of bibtexparser [Boulogne2022].







	References:
	+ [Boulogne2022]
		- Francois Boulogne, Michael Weiss, and sciunto, "bibtexparser 1.4.0," Python Software Foundation, Beaverton, OR, September 23, 2022. Available online from *PyPI -- The Python Package Index: pew 1.4.0* at: https://pypi.org/project/bibtexparser/; February 25, 2023 was the last accessed date.
	+ [Boulogne2023a]
		- Fran{\c{c}}ois Boulogne, Olivier Mangin, Lucas Verney, and other contributors, "Tutorial," Read the Docs, Inc., Portland, OR, January 3, 2023. Available online from *Read the Docs: Welcome to BibtexParser's documentation!: Tutorial* as Version 1.4.0 at: https://bibtexparser.readthedocs.io/en/master/tutorial.html; February 25, 2023 was the last accessed date.
	+ [DrakeJr2023a]
		- Fred L. Drake, Jr., David Goodger, and Fredrik Lundh, "The Python Standard Library," Python Software Foundation, Beaverton, OR, February 26, 2023. Available online from *Welcome to Python.org: Docs: Python 3.11.2 documentation: Library Reference* at: https://docs.python.org/3/library/; February 26, 2023 was the last accessed date.



	



	Revision History:
	February 25, 2023			Version 0.1, initial build.
"""

#	The MIT License (MIT)

#	Copyright (c) <2023> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?

#	==========================================================

__author__ = 'Zhiyang Ong'
__version__ = '0.1'
__date__ = 'February 25, 2025'

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

#	Import Python Modules from installed Python packages, via PyPI


# Requires the following installation.
#pip install bibtexparser
# Import [Boulogne2022] [Boulogne2023a]
import bibtexparser




###############################################################

#	Import Custom Python Modules

# Module to process input arguments to the script/program.
#from utilities.queue_ip_arguments import queue_ip_args
# Module to perform file I/O (input/output) operations.
#from utilities.file_io import file_io_operations


# Module for timing measurements.
from timing_measurements.performance_measurement_no_ns import execution_time_measurement_no_ns

###############################################################




###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	#	= Set up loading of BibTeX database
	# Type of current time measurement.
	mode_current_time_measurement = "perf_counter"
	# Set the initial timestamp.
	execution_time_measurement_no_ns.set_initial_timestamp()
	"""
		Filename/path of the output file that contains the extracted BibTeX entries.
	"""
	output_filename = "./output-files/extracted_bibtext_entries.bib"
	# --------------------------------------------------------
	"""
		Process the input arguments [DrakeJr2023a, from Python Runtime Services: sys — System-specific parameters and functions: sys.argv].

		https://docs.python.org/3/library/sys.html
	"""
	# --------------------------------------------------------
	"""
		Check if the output filename is valid [DrakeJr2023a, from Generic Operating System Services: os — Miscellaneous operating system interfaces: Files and Directories].

		https://docs.python.org/3/library/os.html#os.access
		https://docs.python.org/3/library/os.html#os.W_OK
	"""
	if os.access(output_filename, os.W_OK):
		print("	Filename/Path to target output filename is valid:",output_filename,"=")
	else:
		print(">	Filename/Path to target output filename is invalid:",output_filename,"=")
		"""
			Get the absolute path containing the target output file.

			https://docs.python.org/3/library/os.path.html#os.path.abspath
		"""
		absolute_path_of_target_output_file = os.path.abspath(output_filename)
		print("	Path of target output:",absolute_path_of_target_output_file,"=")
		"""
			This approach only grabs the filename.
		path_of_directory_for_target_output_file = os.path.basename(output_filename)
		print("	Path of the directory for target output:",path_of_directory_for_target_output_file,"=")
		"""
		"""
			Get the path of the directory that would contain the target output file.

			https://docs.python.org/3/library/os.path.html#os.path.dirname
		"""
		path_of_directory_for_target_output_file = os.path.dirname(absolute_path_of_target_output_file)
		print("	Path of the directory for target output:",path_of_directory_for_target_output_file,"=")
		"""
			Is directory that would contain output file a valid directory?

			https://docs.python.org/3/library/os.path.html#os.path.isdir
		"""
		if os.path.isdir(path_of_directory_for_target_output_file):
			print("	Path of the directory for target output is valid.")
			print("	Target output file can be created.")
		else:
			print("	Path of the directory for target output is INVALID!!!")
			print("	Target output file cannot be created!!!")
			print("	Please kindly select path for output file in an existing directory!!!")
	# --------------------------------------------------------
	"""
		Load the BibTeX database as an input file object for the
			parser [Boulogne2023a].

		Run this in the ./outputs/ subdirectory of the BibTeX
			database repository.
	"""
#	with open('../references.bib') as bibtex_file:
		# Load the BibTeX database to the parser.
#	    bib_database = bibtexparser.load(bibtex_file)
	"""
		Print the BibTeX entries of the BibTeX database as a list of
			dictionaries [Boulogne2023a].

		The list of BibTeX entries is stored in: bib_database.entries.
	"""
#	print(bib_database.entries)
	#for bib_entry in bib_database.entries:
	# --------------------------------------------------------
	# Print comments in the BibTeX database as a list of strings.
	#print(bib_database.comments)
	# Print preamble of BibTeX database, which does nothing.
	#print(bib_database.preambles)
	# Print ordered dictionary representing months and their abbreviation.
	#print(bib_database.strings)
	# --------------------------------------------------------
	# Get the elapsed time.
	elapsed_time = execution_time_measurement_no_ns.get_elapsed_time(mode_current_time_measurement)
	#temp_text = "Elapsed time:::"+str(datetime.timedelta(seconds=elapsed_time))+"=\n"
	print("Elapsed time:::",datetime.timedelta(seconds=elapsed_time),"=")