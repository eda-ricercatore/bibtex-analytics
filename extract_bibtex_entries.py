#!/usr/local/bin/python3


"""
	This is written by Zhiyang Ong to extract a subset of BibTeX entries
		from a BibTeX database, using a non-empty subset of the following:
	+ a set of BibTeX keys
	+ a set of keyphrases, stored as optional metadata for each BibTeX entry



	Synopsis: command name and [argument(s)]
	./extract_bibtex_entries.py [-h] [input BibTeX file] [-k] [set of BibTeX keys stored as a CSV file] [-m] [set of keyphrases stored as a CSV file]
	./extract_bibtex_entries.py [-h] [input BibTeX file] [-k] [set of BibTeX keys stored as a CSV file]
	./extract_bibtex_entries.py [-h] [input BibTeX file] [-m] [set of keyphrases stored as a CSV file]
	./extract_bibtex_entries.py [-h] [input BibTeX file] [-k] [set of BibTeX keys stored as a CSV file] [-m] [set of keyphrases stored as a CSV file] 


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
									full name, first/given name, or last name
									(or surname).


	[-b]:					If an optional "-y" flag is used as an
							input argument, accept the following string
								as the booktitle to search for in the
								BibTeX database.
								This is used to extract a subset of
									BibTeX entries that match this
									booktitle.

	[-j]:					If an optional "-j" flag is used as an
							input argument, accept the following string
								as the title of the journal to search
								for in the BibTeX database.
								This is used to extract a subset of
									BibTeX entries that match this
									journal title.

	[-s]:					If an optional "-s" flag is used as an
							input argument, accept the following string
								as the series of books to search for
								in the BibTeX database.
								This is used to extract a subset of
									BibTeX entries that match this series.

	[-u]:					If an optional "-u" flag is used as an
							input argument, accept the following string
								as the school to search for in the
								BibTeX database.
								This is used to extract a subset of
									BibTeX entries that match this
									university.




	Its procedure is described as follows:
	
	Process input arguments.
	If the [-h] input argument/option is selected,
		print the help text with the synopsis of the command name
		and argument(s).
	Open an input file stream for the BibTeX database.
	Parse the BibTeX database, via a BibTeX parser and the file stream.
	Open an input file stream for the CSV input file(s).
	Parse the CSV file, via CSV import, pandas, and the file stream.
	Enumerate each BibTeX entry in the input BibTeX database.
		If the [-k] input argument/option is selected,
			find the set of records (of BibTeX entries) that
			have BibTeX keys found in the set of BibTeX keys,
			and print out information about these records into
			an output file.
			If the [-k] input argument/option is also selected,
				find the subset of these records that have keyphrases
				found in the set of keyphrases, and print out information about these records into an output file.
			Similarly, if multiple options are selected, process them here.
		If the [-k] input argument/option is selected,
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
				the full name, first/given name, or last name (or surname).
				Matches have to be exact.
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

		



	Notes/Assumptions:
	Assume that the 'Keywords' standard BibTeX field is a single line
		field.
	Assume that each pair of keywords, or keyphrases, is separated by
		", " in the 'Keywords' fields of the BibTeX database, and by
		"," in the CSV file.
	CSV refers to comma-separated values, and is a delimited text file
		that uses commas (or ",") to separate/delimit values.


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

