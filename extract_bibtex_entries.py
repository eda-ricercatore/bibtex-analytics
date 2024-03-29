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
	Open a BibTeX database, and create an input file object for it.
	Parse the BibTeX database, via a BibTeX parser and the file object.
	Open CSV input file(s), and create an input file object for each
		CSV input file.
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

	If options are used multiple times, only the last instance
		associated with that option is used.

	
	The following variables are associated with paired/2-tuples input
		arguments:
	+ bibtex_key_csv_filename
	+ keyphrases_csv_filename
	+ names_of_all_authors
	+ last_name_of_an_author
	+ booktitle_selected
	+ journal_title
	+ series_title
	+ university_name
	If these variables have the value of "None", this implies that
		their corresponding paired/2-tuples input arguments are not
		processed as valid arguments.
		Hence, such "None"-valued variables would not be processed as
			their corresponding paired/2-tuples input arguments are
			not correctly selected/chosen.





	Requirements:
	+ Installation of bibtexparser [Boulogne2022, from Step 3: Export: Call the writer].







	References:
	+ [Boulogne2022]
		- Francois Boulogne, Michael Weiss, and sciunto, "bibtexparser 1.4.0," Python Software Foundation, Beaverton, OR, September 23, 2022. Available online from *PyPI -- The Python Package Index: pew 1.4.0* at: https://pypi.org/project/bibtexparser/; February 25, 2023 was the last accessed date.
	+ [Boulogne2023a]
		- Fran{\c{c}}ois Boulogne, Olivier Mangin, Lucas Verney, and other contributors, "Tutorial," Read the Docs, Inc., Portland, OR, January 3, 2023. Available online from *Read the Docs: Welcome to BibtexParser's documentation!: Tutorial* as Version 1.4.0 at: https://bibtexparser.readthedocs.io/en/master/tutorial.html; February 25, 2023 was the last accessed date.
	+ [Boulogne2023b]
		- Fran{\c{c}}ois Boulogne, Olivier Mangin, Lucas Verney, and other contributors, "bibtexparser: API," Read the Docs, Inc., Portland, OR, January 3, 2023. Available online from *Read the Docs: Welcome to BibtexParser's documentation!: bibtexparser: API* as Version 1.4.0 at: https://bibtexparser.readthedocs.io/en/master/bibtexparser.html; February 28, 2023 was the last accessed date.
	+ [DrakeJr2023a]
		- Fred L. Drake, Jr., David Goodger, and Fredrik Lundh, "The Python Standard Library," Python Software Foundation, Beaverton, OR, February 26, 2023. Available online from *Welcome to Python.org: Docs: Python 3.11.2 documentation: Library Reference* at: https://docs.python.org/3/library/; February 26, 2023 was the last accessed date.
	+ [DrakeJr2023b]
		- Fred L. Drake, Jr., David Goodger, and Fredrik Lundh, "The Python Tutorial," Python Software Foundation, Beaverton, OR, February 26, 2023. Available online from *Welcome to Python.org: Docs: Python 3.11.2 documentation: Tutorial* at: https://docs.python.org/3/tutorial/; February 26, 2023 was the last accessed date.
	+ [Miles2013]
		- Alistair Miles, "csvvalidator 1.2," Python Software Foundation, Beaverton, OR, May 16, 2013. Available online from *PyPI -- The Python Package Index: csvvalidator 1.2* as Version 1.2 at: https://pypi.org/project/csvvalidator/; February 25, 2023 was the last accessed date.




	



	



	Revision History:
	February 25, 2023			Version 0.1, initial build.
	March 2, 2023 				Version 1.0, initial version.
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
"""
	Workaround to address the following (run-time) error/bug.

	AttributeError: type object 'datetime.datetime' has no attribute 'timedelta'
"""
from datetime import timedelta
"""
	Import the CSV [Miles2013] [DrakeJr2023a, from File Formats: csv — CSV File Reading and Writing].

	https://docs.python.org/3/library/csv.html
"""
import csv
# To enable testing the Python "multiset" approach.
from collections import Counter


###############################################################

#	Import Python Modules from installed Python packages, via PyPI


# Requires the following installation.
#pip install bibtexparser
#pip install csvvalidator

# Import [Boulogne2022] [Boulogne2023a].
import bibtexparser
# Import [Boulogne2023a].
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

"""
	Import [Miles2013].
	This Python package from PyPI causes problems with finding
		the method: datetime.timedelta()
	
	A workaround is described as follows.

	Import the following in addition to: "import datetime"
	from datetime import timedelta

	Subsequently, use the following method call instead.

	timedelta()
"""
#import csvvalidator
from csvvalidator import *




###############################################################

#	Import Custom Python Modules

# Module to process input arguments to the script/program.
#from utilities.queue_ip_arguments import queue_ip_args
# Module to perform file I/O (input/output) operations.
#from utilities.file_io import file_io_operations


# Module for timing measurements.
from timing_measurements.performance_measurement_no_ns import execution_time_measurement_no_ns


###############################################################



#	= Set up loading of BibTeX database
# Type of current time measurement.
mode_current_time_measurement = "perf_counter"
# Set the initial timestamp.
execution_time_measurement_no_ns.set_initial_timestamp()


# Options for the script.
# [-h] option for the script.
h_option = "-h"
# [-k] option for the script.
k_option = "-k"
# [-m] option for the script.
m_option = "-m"
# [-a] option for the script.
a_option = "-a"
# [-z] option for the script.
z_option = "-z"
# [-b] option for the script.
b_option = "-b"
# [-j] option for the script.
j_option = "-j"
# [-s] option for the script.
s_option = "-s"
# [-u] option for the script.
u_option = "-u"


# Filename/path to the input CSV file containing a set of BibTeX keys.
bibtex_key_csv_filename = None
# Filename/path to the input CSV file containing a set of keyphrases.
keyphrases_csv_filename = None
# Names of all the authors.
names_of_all_authors = None
# Last name of an author.
last_name_of_an_author = None
"""
	Booktitle, or title of a book for a reference to its chapter,
		section, subsection, or subsubsection.
	It can also be the title of a conference proceedings.
"""
booktitle_selected = None
# Title of the journal.
journal_title = None
# Title of the book series, or conference proceedings.
series_title = None
# Name of a research university that grants advanced/research degrees.
university_name = None

"""
	Dictionary of non-None -valued variables corresponding to paired/2-tuples
		input arguments, and their values.

	bibtex_key_csv_filename, keyphrases_csv_filename, names_of_all_authors, last_name_of_an_author, booktitle_selected, journal_title, series_title, university_name

	Rather than add all these variables to the dictionary, and check
		if their value is "None", only add variables and their
		corresponding values if they have been processed as valid
		input arguments.
		This avoids having to check if a variable has the value of "None".
	Do this in the corresponding "if" or "else if" block when processing
		these paired/2-tuples input arguments.
	Using a dictionary, or another data structure of (key,value) pairs
		for these paired/2-tuples input arguments allows us to avoid enumerating
		the set of all BibTeX entries for each variable.
		This slightly increases the duration of the iteration/enumeration
			of the set of all BibTeX entries, but avoids enumerating this set
			multiple times (eight as of February 27, 2023).
"""
paired_input_arguments = {}


# Error flags for sys.exit() method calls.
"""
	Incorrect usage of paired input arguents, such as:
		[-k] [-m] [-a] [-z] [-b] [-j] [-s] [-u]
"""
incorrect_usage_of_paired_input_arguments = 1
# Input filename is invalid.
input_filename_is_invalid = 2
# Output filename, or path of output file, is invalid.
output_filename_or_path_is_invalid = 3


# BibTeX database that would be parsed and processed.
input_bibtex_file = "../references.bib"

###############################################################

"""
	Method to print the "help" manual for this script, and a synopsis
		of how to use it, using the name of this script and set of
		acceptable input arguments.
	@param None - No input arguments.
	@return Nothing.
"""
def print_help_manual():
	print("--------------------------------------------------------")
	print("")
	print("Synopsis of using: extract_bibtex_entries.py")
	print("")
	print("./extract_bibtex_entries.py [-h] [-k] [input CSV file] [-m] [input CSV file] [-a] [string] [-z] [string] [-b] [string] [-j] [string] [-s] [string] [-u] [string]")
	print("")
	print("The only unary input argument is: [-h]")
	print("")
	print("Other input arguments come in pairs, 2-tuples: [flag] [filename or string]")
	print("")
	print("Acceptable flags for 2-tuples input arguments are: [-k] [-m] [-a] [-z] [-b] [-j] [-s] [-u]")
	print("")




"""
	Method to validate a comma-separated values (CSV) file.
	@param csv_filename - Filename of the CSV file to be validated.
	@return boolean True, if csv_filename is a valid CSV file;
		else, return False.
"""
def validate_csv_file(csv_filename=None):
	#print("	csv_filename is:",csv_filename,"=")
	if None != csv_filename:
		validator = CSVValidator("Generic CSV file")
		csv_data = csv.reader(csv_filename)
		problems_with_csv_file = validator.validate(csv_data)
		#print("	problems_with_csv_file is:",problems_with_csv_file,"=")
		if not problems_with_csv_file:
			#print("	There are no problems with the CSV file.")
			return True
		else:
			#print("	There are problems with the CSV file!!!")
			#print("	problems_with_csv_file is:",problems_with_csv_file,"=")
			return False
	else:
		#print("	The csv_filename is:",csv_filename,"=")
		#print("	csv_filename is NOT 'None'.")
		return False





"""
	Method to determine if selected input arguments have been selected.
	@param dict_key_to_ip_arg - Variable name storing the input argument's
		value that contains a filename of a CSV file.
	@param text_about_ip_arg - Stores information/text about the input
		argument to be processed.
	@return Nothing.


	Notes:
	Handle each input argument with if-else statements, rather than
		if-elif-...-elif-else statements, since the former allows
		multiple input arguments with input filenames to be used
		concurrently while the latter can only support one input
		argument with input filename to be processed per set of
		if-elif-...-elif-else statements.
		Hence, the latter would require multiple sets of such statements
			to enable concurrent input arguments to include input
			filenames.
"""
def is_x_input_argument_selected_for_csv_file(dict_key_to_ip_arg=None,text_about_ip_arg=None):
	# Is the [-?] option (indicated by dict_key_to_ip_arg) selected?
	if None != paired_input_arguments.get(dict_key_to_ip_arg):
		"""
			Yes, load the input CSV file.
			Check of the input CSV file for BibTeX keys is valid.
		"""
		dict_val_to_ip_arg = paired_input_arguments.get(dict_key_to_ip_arg)
		if validate_csv_file(csv_filename=dict_val_to_ip_arg):
			print("	No problems with the CSV file for BibTeX keys.")
			"""
				Read the CSV file for BibTeX keys [DrakeJr2023a, from File Formats: csv — CSV File Reading and Writing].

				https://docs.python.org/3/library/csv.html
			"""
			#bibtex_keys_selected = csv.reader(dict_val_to_ip_arg, delimiter=',', quotechar='|')
			with open(dict_val_to_ip_arg, "r") as csv_ip_file_obj:
				dict_val_to_ip_arg_csv_obj = csv.reader(csv_ip_file_obj, delimiter=',')
				print("Value of",dict_key_to_ip_arg,"is:",dict_val_to_ip_arg_csv_obj,"=")
				for row in dict_val_to_ip_arg_csv_obj:
					paired_input_arguments[dict_key_to_ip_arg] = row
					print("	List of", text_about_ip_arg, "are:",paired_input_arguments[dict_key_to_ip_arg],"=")
			print("paired_input_arguments[",dict_key_to_ip_arg,"] has been updated:",paired_input_arguments[dict_key_to_ip_arg],"=")
		else:
			print("	There are problems with the CSV file for BibTeX keys!!!")
			# End execution of the script to indicate error.
			sys.exit(input_filename_is_invalid)
	else:
		# Else, no, proceed/continue/pass.
		print("This input argument with input file is not used:",dict_key_to_ip_arg,"=")


"""
	Method to determine if a list of keyphrases is a subset of another,
		using the Python approach for multisets [Karefylakis2013] and
		set difference [WikipediaContributors2023] [WikipediaContributors2023a] [WikipediaContributors2023b] [Kenny2017].
	@param string_representation_of_bigger_list - a string representation
		of bigger list of strings/keyphrases that we want to determine
		if it is the superset.
	@param smaller_list - a smaller list of strings/keyphrases that
		we want to determine if it is the subset.
	@return boolean True, if the smaller list is a subset of the bigger
		list; else, return False.
"""
def is_list_a_subset_of_another_multiset_method_with_comparisons_with_preprocessing(string_representation_of_bigger_list=None, smaller_list=None):
	bigger_list = string_representation_of_bigger_list.split(", ")
	return is_list_a_subset_of_another_multiset_method_with_comparisons(bigger_list, smaller_list)
	#return is_list_a_subset_of_another(bigger_list, smaller_list)
	#return is_list_a_subset_of_another_enumerate(bigger_list, smaller_list)







"""
	Method to determine if a list is a subset of another, using the Python
		approach for multisets [Karefylakis2013] and set difference
		[WikipediaContributors2023] [WikipediaContributors2023a] [WikipediaContributors2023b] [Kenny2017].
	@param bigger_list - a bigger list of items that we want to determine
		if it is the superset.
	@param smaller_list - a smaller list of items that we want to determine
		if it is the subset.
	@return boolean True, if the smaller list is a subset of the bigger list;
		else, return False.
"""
def is_list_a_subset_of_another_multiset_method_with_comparisons(bigger_list=None, smaller_list=None):
	# Is the smaller list actually bigger than the bigger list?
	if len(smaller_list) > len(bigger_list):
		# Yes, return False.
		return False
		"""
			Do not swap files of different sizes, since we want
				BibTeX entries with all the keyphrases.
			Else, it will accept BibTeX entries with one keyphrase,
				whenn all the selected keyphrases are wanted in BibTeX
				entries.

		# Yes, swap these two lists.
		temp_list = bigger_list
		bigger_list = smaller_list
		smaller_list = temp_list
		"""
	# Is the bigger or smaller list referencing the 'None' object? 
	if (bigger_list is None) or (smaller_list is None):
		# Yes, return False.
		return False
	else:
		"""
			Else, does the value of a key in smaller list greater than
				the value of the same key in the bigger list, by
				using the Counter ">" operator to do the comparison?
		"""
		bigger_count = Counter(bigger_list)
		smaller_count = Counter(smaller_list)
		"""
			Enumerate each key in the smaller Counter object or multiset.

			Counter no longer has a has_key() method [DrakeJr2023a].

			Use the "in" operator (or contains(seq, obj) function)
				instead [Kenny2017] [Guerrero2022] [Nguyen2019] [Reddy2018].


			[DrakeJr2023a, from Functional Programming Modules: operator — Standard operators as functions]
			https://docs.python.org/3/library/operator.html#operator.contains


			[DrakeJr2023a, from Functional Programming Modules: operator — Standard operators as functions: Mapping Operators to Functions]
			https://docs.python.org/3/library/operator.html#mapping-operators-to-functions
		"""
		for key in smaller_count:
			"""
				For the currently enumerated key (or key-value pair)
					in the smaller list or Counter object, is it not
					found in the larger list or Counter object?
			"""
			if (key in bigger_count) == False:
				# It is not found in the larger list or Counter object.
				return False
			"""
				Is item of the smaller list, or key of the smaller
					Counter, occuring more in the smaller list than
					in the bigger list?

				For the currently enumerated key (or key-value pair)
					in the smaller list, is its value greater than
					that of the larger list?
			"""
			if smaller_count[key] > bigger_count[key]:
				"""
					Yes, the smaller list has more instances of an
						item than the bigger list.
				"""
				return False
		return True





"""
	Method to determine if a list is a subset of another, using the Python
		"universal quantifier" operator, all() [DrakeJr2023a, from Built-in Functions]
		[manjeet042023].
	@param bigger_list - a bigger list of items that we want to determine
		if it is the superset.
	@param smaller_list - a smaller list of items that we want to determine
		if it is the subset.
	@return boolean True, if the smaller list is a subset of the bigger list;
		else, return False.


	References:
	+ URL for [DrakeJr2023a, from Built-in Functions]
		- https://docs.python.org/3/library/functions.html#all
		- https://docs.python.org/3/library/functions.html#any
"""
def is_list_a_subset_of_another(bigger_list=None, smaller_list=None):
	# Is the smaller list actually bigger than the bigger list?
	if len(smaller_list) > len(bigger_list):
		# Yes, return False.
		return False
		"""
		# Yes, swap these two lists.
		temp_list = bigger_list
		bigger_list = smaller_list
		smaller_list = temp_list
		"""
	# Is the bigger or smaller list referencing the 'None' object? 
	if (bigger_list is None) or (smaller_list is None):
		# Yes, return False.
		return False
	else:
		"""
			Else, are all the elements/items in the smaller list found
				in the bigger?
		"""
		if all(x in bigger_list for x in smaller_list):
			# Yes.
			return True
		else:
			# No.
			return False




"""
	Method to determine if a list is a subset of another, by checking
		if each element in the smaller list is found in the bigger
		list.
	@param bigger_list - a bigger list of items that we want to determine
		if it is the superset.
	@param smaller_list - a smaller list of items that we want to determine
		if it is the subset.
	@return boolean True, if the smaller list is a subset of the bigger list;
		else, return False.
"""
def is_list_a_subset_of_another_enumerate(bigger_list=None, smaller_list=None):
	# Is the smaller list actually bigger than the bigger list?
	if len(smaller_list) > len(bigger_list):
		# Yes, return False.
		return False
		"""
		# Yes, swap these two lists.
		temp_list = bigger_list
		bigger_list = smaller_list
		smaller_list = temp_list
		"""
	# Is the bigger or smaller list referencing the 'None' object?
	if (bigger_list is None) or (smaller_list is None):
		# Yes, return False.
		return False
	else:
		"""
			For each elements/items in the smaller list, is it found
				in the bigger list?
		"""
		for item in smaller_list:
			if item not in bigger_list:
				# No.
				return False
			else:
				# Yes. Enumerate the next item in the smaller list.
				continue
		# Each item in the smaller list is found in the bigger list.
		return True









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
	# Number of input arguments for this Python script.
	number_of_input_arguments = len(sys.argv)
	"""
		Are there any input arguments?

		sys.argv contains at least one element, which is the name of the
			Python script being executed, and is indicated by sys.argv[0].

		Input arguments for the Python script being executed have indices
			that range from 1 to "n", if "n" input arguments are provided.
	"""
	if 1 < number_of_input_arguments:
		# Yes. Is the [-h] option/flag is used?
		if h_option in sys.argv:
			# Yes, print the help manual. Skip subsequent processing of [-h].
			print_help_manual()
			"""
				Is the number of input arguments 1?

				The comparison is made with 2, since sys.argv includes
					the name of the scripts as an (input) argument.
			"""
			if 2 == number_of_input_arguments:
				# Yes. End execution of the script without error.
				exit(0)
		"""
			Enumerate the options of the program.

			If the [-h] option is encountered, skip its processing.
		"""
		# List of input arguments.
		iterator_for_list_of_input_arguments = enumerate(sys.argv[1:])
		#for index, option in enumerate(sys.argv[1:]):
		for index, option in iterator_for_list_of_input_arguments:
			# Is this input argument the [-h] option?
			if h_option == option:
				"""
					Yes, skip its processing [DrakeJr2023b, from Section 4. More Control Flow Tools: Subsection 4.4. break and continue Statements, and else Clauses on Loops]

					https://docs.python.org/3/tutorial/controlflow.html
				"""
				continue
			elif k_option == option:
				print("= Processing the [-k] option.")
				print("index is:",index,"=")
				print("option is:",option,"=")
				# Is there at least one more input argument to process?
				if index < number_of_input_arguments:
					#index = index + 1
					print("= Filename of input CSV file for the [-k] option.")
					print("index is:",index+1,"=")
					"""
						Process the next input argument that should contain
							the valid input filename for a CSV file.
					"""
					bibtex_key_csv_filename = next(iterator_for_list_of_input_arguments)[1]
					print("option is:",bibtex_key_csv_filename,"=")
					"""
						Is the filename/path for the CSV file containing BibTeX keys valid?

						Or, does that file or path exist?
					"""
					if not os.path.isfile(bibtex_key_csv_filename):
						# No, it does not exist.
						print(">>>	BibTeX keys CSV filename is invalid:", bibtex_key_csv_filename,"=")
						# End execution of the script to indicate error.
						sys.exit(incorrect_usage_of_paired_input_arguments)
					else:
						print("	BibTeX keys CSV filename is valid:", bibtex_key_csv_filename,"=")
						"""
							Add "bibtex_key_csv_filename" and its value
								to the dictionary of paired input
								arguments for subsequent processing.
						"""
						paired_input_arguments["bibtex_key_csv_filename"] = bibtex_key_csv_filename
				else:
					"""
						No, there are no more input arguments to process.

						The [-k] option requires a pair of input arguments.
						+ the [-k] flag
						+ valid input filename for a CSV file
					"""
					print("	Invalid usage of [-k] option.")
					print("	No valid input filename for a CSV file is provided for the [-k] option.")
					print("")
					print_help_manual()
					# End execution of the script to indicate error.
					sys.exit(incorrect_usage_of_paired_input_arguments)
			elif m_option == option:
				print("= Processing the [-m] option.")
				print("index is:",index,"=")
				print("option is:",option,"=")
				# Is there at least one more input argument to process?
				if index < number_of_input_arguments:
					#index = index + 1
					print("= Filename of input CSV file for the [-m] option.")
					print("index is:",index+1,"=")
					"""
						Process the next input argument that should contain
							the valid input filename for a CSV file.
					"""
					keyphrases_csv_filename = next(iterator_for_list_of_input_arguments)[1]
					print("option is:",keyphrases_csv_filename,"=")
					"""
						Is the filename/path for the CSV file containing keyphrases valid?

						Or, does that file or path exist?
					"""
					if not os.path.isfile(keyphrases_csv_filename):
						# No, it does not exist.
						print(">>>	Keyphrases CSV filename is invalid:", keyphrases_csv_filename,"=")
						# End execution of the script to indicate error.
						sys.exit(incorrect_usage_of_paired_input_arguments)
					else:
						print("	Keyphrases CSV filename is valid:", keyphrases_csv_filename,"=")
						"""
							Add "keyphrases_csv_filename" and its value
								to the dictionary of paired input
								arguments for subsequent processing.
						"""
						paired_input_arguments["keyphrases_csv_filename"] = keyphrases_csv_filename
				else:
					"""
						No, there are no more input arguments to process.

						The [-m] option requires a pair of input arguments.
						+ the [-m] flag
						+ valid input filename for a CSV file
					"""
					print("	Invalid usage of [-m] option.")
					print("	No valid input filename for a CSV file is provided for the [-m] option.")
					print("")
					print_help_manual()
					# End execution of the script to indicate error.
					sys.exit(incorrect_usage_of_paired_input_arguments)
			elif a_option == option:
				print("= Processing the [-a] option.")
				print("index is:",index,"=")
				print("option is:",option,"=")
				# Is there at least one more input argument to process?
				if index < number_of_input_arguments:
					#index = index + 1
					print("= Names of authors for the [-a] option.")
					print("index is:",index+1,"=")
					"""
						Process the next input argument that should contain
							the names of authors of selected publications.
					"""
					names_of_all_authors = next(iterator_for_list_of_input_arguments)[1]
					print("option is:",names_of_all_authors,"=")
					"""
						Add "names_of_all_authors" and its value to
							the dictionary of paired input arguments
							for subsequent processing.
					"""
					paired_input_arguments["names_of_all_authors"] = names_of_all_authors
				else:
					"""
						No, there are no more input arguments to process.

						The [-a] option requires a pair of input arguments.
						+ the [-a] flag
						+ names of authors
					"""
					print("	Invalid usage of [-a] option.")
					print("	No names of authors are provided for the [-a] option.")
					print("")
					print_help_manual()
					# End execution of the script to indicate error.
					sys.exit(incorrect_usage_of_paired_input_arguments)
			elif z_option == option:
				print("= Processing the [-z] option.")
				print("index is:",index,"=")
				print("option is:",option,"=")
				# Is there at least one more input argument to process?
				if index < number_of_input_arguments:
					#index = index + 1
					print("= Last name of an author for the [-z] option.")
					print("index is:",index+1,"=")
					"""
						Process the next input argument that should contain
							the last name of an author of selected publications.
					"""
					last_name_of_an_author = next(iterator_for_list_of_input_arguments)[1]
					print("option is:",last_name_of_an_author,"=")
					"""
						Add "last_name_of_an_author" and its value to
							the dictionary of paired input arguments
							for subsequent processing.
					"""
					paired_input_arguments["last_name_of_an_author"] = last_name_of_an_author
				else:
					"""
						No, there are no more input arguments to process.

						The [-z] option requires a pair of input arguments.
						+ the [-z] flag
						+ last name of an author
					"""
					print("	Invalid usage of [-z] option.")
					print("	No last name of an author is provided for the [-z] option.")
					print("")
					print_help_manual()
					# End execution of the script to indicate error.
					sys.exit(incorrect_usage_of_paired_input_arguments)
			elif b_option == option:
				print("= Processing the [-b] option.")
				print("index is:",index,"=")
				print("option is:",option,"=")
				# Is there at least one more input argument to process?
				if index < number_of_input_arguments:
					#index = index + 1
					print("= Booktitle for the [-b] option.")
					print("index is:",index+1,"=")
					"""
						Process the next input argument that should contain
							the booktitle of selected publications.
					"""
					booktitle_selected = next(iterator_for_list_of_input_arguments)[1]
					print("option is:",booktitle_selected,"=")
					"""
						Add "booktitle_selected" and its value to
							the dictionary of paired input arguments
							for subsequent processing.
					"""
					paired_input_arguments["booktitle_selected"] = booktitle_selected
				else:
					"""
						No, there are no more input arguments to process.

						The [-b] option requires a pair of input arguments.
						+ the [-b] flag
						+ booktitle
					"""
					print("	Invalid usage of [-b] option.")
					print("	No booktitle is provided for the [-b] option.")
					print("")
					print_help_manual()
					# End execution of the script to indicate error.
					sys.exit(incorrect_usage_of_paired_input_arguments)
			elif j_option == option:
				print("= Processing the [-j] option.")
				print("index is:",index,"=")
				print("option is:",option,"=")
				# Is there at least one more input argument to process?
				if index < number_of_input_arguments:
					#index = index + 1
					print("= Journal title for the [-j] option.")
					print("index is:",index+1,"=")
					"""
						Process the next input argument that should contain
							the journal title of selected publications.
					"""
					journal_title = next(iterator_for_list_of_input_arguments)[1]
					print("option is:",journal_title,"=")
					"""
						Add "journal_title" and its value to
							the dictionary of paired input arguments
							for subsequent processing.
					"""
					paired_input_arguments["journal_title"] = journal_title
				else:
					"""
						No, there are no more input arguments to process.

						The [-j] option requires a pair of input arguments.
						+ the [-j] flag
						+ journal title
					"""
					print("	Invalid usage of [-j] option.")
					print("	No journal title is provided for the [-j] option.")
					print("")
					print_help_manual()
					# End execution of the script to indicate error.
					sys.exit(incorrect_usage_of_paired_input_arguments)
			elif s_option == option:
				print("= Processing the [-s] option.")
				print("index is:",index,"=")
				print("option is:",option,"=")
				# Is there at least one more input argument to process?
				if index < number_of_input_arguments:
					#index = index + 1
					print("= Series title for the [-s] option.")
					print("index is:",index+1,"=")
					"""
						Process the next input argument that should contain
							the book series title of selected publications.
					"""
					series_title = next(iterator_for_list_of_input_arguments)[1]
					print("option is:",series_title,"=")
					"""
						Add "series_title" and its value to
							the dictionary of paired input arguments
							for subsequent processing.
					"""
					paired_input_arguments["series_title"] = series_title
				else:
					"""
						No, there are no more input arguments to process.

						The [-s] option requires a pair of input arguments.
						+ the [-s] flag
						+ book series title
					"""
					print("	Invalid usage of [-s] option.")
					print("	No book series title is provided for the [-s] option.")
					print("")
					print_help_manual()
					# End execution of the script to indicate error.
					sys.exit(incorrect_usage_of_paired_input_arguments)
			elif u_option == option:
				print("= Processing the [-u] option.")
				print("index is:",index,"=")
				print("option is:",option,"=")
				# Is there at least one more input argument to process?
				if index < number_of_input_arguments:
					#index = index + 1
					print("= University name for the [-u] option.")
					print("index is:",index+1,"=")
					"""
						Process the next input argument that should contain
							the university name of Masters theses and Ph.D.
							dissertations.
					"""
					university_name = next(iterator_for_list_of_input_arguments)[1]
					print("option is:",university_name,"=")
					"""
						Add "university_name" and its value to
							the dictionary of paired input arguments
							for subsequent processing.
					"""
					paired_input_arguments["university_name"] = university_name
				else:
					"""
						No, there are no more input arguments to process.

						The [-u] option requires a pair of input arguments.
						+ the [-u] flag
						+ university name
					"""
					print("	Invalid usage of [-u] option.")
					print("	No university name is provided for the [-u] option.")
					print("")
					print_help_manual()
					# End execution of the script to indicate error.
					sys.exit(incorrect_usage_of_paired_input_arguments)
			else:
				# Else, process the next input argument.
				print("index is:",index,"=")
				print("option is:",option,"=")
	else:
		# No, print the help manual.
		print_help_manual()
		# End execution of the script without error.
		sys.exit(0)
	# --------------------------------------------------------
	
	"""
		Do additional preprocessing of input CSV files, so that the
			loading and processing of these files only have to be
			done once, rather than multiple times in a "for" loop
			that iterates through the set of BibTeX entries.
	"""
	is_x_input_argument_selected_for_csv_file("bibtex_key_csv_filename","BibTeX keys")
	is_x_input_argument_selected_for_csv_file("keyphrases_csv_filename","keyphrases")
	# --------------------------------------------------------
	"""
		Check if the output filename is valid [DrakeJr2023a, from Generic Operating System Services: os — Miscellaneous operating system interfaces: Files and Directories].

		https://docs.python.org/3/library/os.html#os.access
		https://docs.python.org/3/library/os.html#os.W_OK


		Use input_file_object.seek(0) to reset the read position to
			the start of the input file.
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
			sys.exit(output_filename_or_path_is_invalid)
	# --------------------------------------------------------
	"""
		Load the BibTeX database as an input file object for the
			parser [Boulogne2023a].

		Run this in the ./outputs/ subdirectory of the BibTeX
			database repository.
	"""
	with open(input_bibtex_file) as bibtex_file:
		# Load the BibTeX database to the parser.
	    bib_database = bibtexparser.load(bibtex_file)
	"""
		Print the BibTeX entries of the BibTeX database as a list of
			dictionaries [Boulogne2023a].

		The list of BibTeX entries is stored in: bib_database.entries.


		Note: Current solution fails to enumerate the BibTeX database
			and remove BibTeX entries that are not selected by input
			arguments.
		E.g., only 10382 out of 20764 BibTeX entries are removed.
		A workaround is to assign matching BibTeX entries to a new
			list, and assign that list to bib_database.entries by
			replacing/overwriting the original set of BibTeX entries.
	"""
	print("paired_input_arguments is:",paired_input_arguments,"=")
#	print("paired_input_arguments[paired_ip_arg] is:",paired_input_arguments["bibtex_key_csv_filename"],"=")
#	print("paired_input_arguments[paired_ip_arg] is:",paired_input_arguments["keyphrases_csv_filename"],"=")
#	print(bib_database.entries)
#	print("Pre-processing - Number of BibTeX entries in bib_database.entries:",len(bib_database.entries),"=")
	filtered_bibtex_entries = []
	"""
		Enumerate the list of BibTeX entries, and process them based
			on the given paired/2-tuples input arguments.

		bibtex_key_csv_filename, keyphrases_csv_filename, names_of_all_authors, last_name_of_an_author, booktitle_selected, journal_title, series_title, university_name


		####TO BE COMPLETED

		Implement the rest of the if-elif-...-elif-else statement for
			the following input arguments/options.
		[-a] [-z] [-b] [-j] [-s] [-u]

		These other options are not that urgent and important.
	"""
	for bib_entry in bib_database.entries:
		# Process BibTeX entry using given paired/2-tuples input arguments.
		for paired_ip_arg in paired_input_arguments:
			# Is a list of BibTeX keys specified?
			if "bibtex_key_csv_filename" == paired_ip_arg:
				"""
					Yes. Determine if the BibTeX key of the current
						BibTeX entry is in the list of selected BibTeX keys.
				"""
				#if bib_entry["ID"] not in paired_input_arguments[paired_ip_arg]:
				if bib_entry["ID"] in paired_input_arguments[paired_ip_arg]:
					"""
						No, it is not in the list of selected BibTeX keys.
						Remove it from the copy of the BibTeX database.
					"""
#					print("	Before removal: Size of bib_database.entries:",len(bib_database.entries),"=")
					#bib_database.entries.remove(bib_entry)
					filtered_bibtex_entries.append(bib_entry)
#					print("	After removal: Size of bib_database.entries:",len(bib_database.entries),"=")
				else:
					#print("	Unremoved BibTeX key is:",bib_entry["ID"],"=")
					pass
			# No. Is the list of keyphrases specified?
			elif "keyphrases_csv_filename" == paired_ip_arg:
				"""
					Yes. Determine if the keyphrases of the current
						BibTeX entry include keyphrases in the list
						of selected BibTeX keys.
				"""
				#if bib_entry["keywords"] not in paired_input_arguments[paired_ip_arg]:
				#if bib_entry["keywords"] in paired_input_arguments[paired_ip_arg]:
				if is_list_a_subset_of_another_multiset_method_with_comparisons_with_preprocessing(bib_entry["keywords"],paired_input_arguments[paired_ip_arg]):
					"""
						No, it is not in the list of selected BibTeX keys.
						Remove it from the copy of the BibTeX database.
					"""
#					print("	Before removal: Size of bib_database.entries:",len(bib_database.entries),"=")
					#bib_database.entries.remove(bib_entry)
					filtered_bibtex_entries.append(bib_entry)
#					print("	After removal: Size of bib_database.entries:",len(bib_database.entries),"=")
				else:
					#print("	Unremoved BibTeX key is:",bib_entry["ID"],"=")
					pass
			else:
				#print("	Other input arguments are selected.")
				pass
	"""
		Print the set of remaining BibTeX entries with the selected
			BibTeX keys.
	"""
#	print("Post-processing - Number of BibTeX entries in bib_database.entries:",len(bib_database.entries),"=")
#	print("Filtered set of BibTeX entries 'filtered_bibtex_entries' is:",filtered_bibtex_entries,"=")
	print("Size of filtered set of BibTeX entries is:",len(filtered_bibtex_entries),"=")
	bib_database.entries = filtered_bibtex_entries
	print("Print the set of remaining BibTeX entries with the selected BibTeX keys.")
	print(bib_database.entries)
	# --------------------------------------------------------
	# Print comments in the BibTeX database as a list of strings.
	#print(bib_database.comments)
	# Print preamble of BibTeX database, which does nothing.
	#print(bib_database.preambles)
	# Print ordered dictionary representing months and their abbreviation.
	#print(bib_database.strings)
	# --------------------------------------------------------
	"""
		Print the set of filtered BibTeX entries to the designated
			BibTeX output file [Boulogne2023a].
	"""
	btx_writer = BibTexWriter()
	"""
		From [Boulogne2023b] to remove comments in generated BibTeX
			output file.
	"""
	btx_writer.contents = ["entries"]
	# Create an output file object for the BibTeX output file.
	with open(output_filename, "w") as bibtex_file_obj:
		# Print the filtered set of BibTeX entries to output file.
		bibtex_file_obj.write(btx_writer.write(bib_database))
	#print("bibtexparser.bibdatabase.BibDatabase.comments is:",bibtexparser.bibdatabase.BibDatabase.comments,"=")
	# --------------------------------------------------------
	# Get the elapsed time.
	elapsed_time = execution_time_measurement_no_ns.get_elapsed_time(mode_current_time_measurement)
	#temp_text = "Elapsed time:::"+str(datetime.timedelta(seconds=elapsed_time))+"=\n"
	"""
		Workaround to address the following (run-time) error/bug.

		AttributeError: type object 'datetime.datetime' has no attribute 'timedelta'
	"""
	#print("Elapsed time:::",datetime.timedelta(seconds=elapsed_time),"=")
	print("Elapsed time:::",timedelta(seconds=elapsed_time),"=")
	print("")
	print("")