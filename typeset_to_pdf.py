#!/Users/zhiyang/anaconda3/bin/python3
###!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	/usr/bin/python
###	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	#!/usr/bin/python -mtimeit


"""
	This Python script is written by Zhiyang Ong to print BibTeX
		entries in my BibTeX database to a list of references in
		a LaTeX/PDF file.

	Synopsis:
	Print BibTeX entries in my BibTeX database to PDF, via LaTeX.

	This script can be executed as follows:
	./typeset_to_pdf.py [-h] [BibTeX file]

	Parameters:
	[input BibTeX file]:	A BibTeX file/database of BibTeX entries.



	Notes/Assumptions:
	Raise an exception concerning the existence of the duplicates,
		when duplicates of a BibTeX key are found.
	Raise an exception when a tokenized BibTeX entry is not a
		standard entry type.
	Raise an exception when a mismatch occurs in determining the
		number of BibTeX entries processed.


	Revision History:
	July 7, 2019		Version 0.1	Testing the first version.
	July 7, 2019		Version 1.0 Working script release.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'July 7, 2019'

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

import sys
import os
import os.path
#from pathlib import Path
import subprocess
from subprocess import call
import time
import warnings
import re



###############################################################
#	Import Custom Python Modules

# Module to process input arguments to the script/program.
from utilities.queue_ip_arguments import queue_ip_args
# Module to perform file I/O (input/output) operations.
from utilities.file_io import file_io_operations




###############################################################
#	Module with methods that clean BibTeX files.
class Typeset_to_LaTeX:
	# List of BibTeX keys
	set_of_BibTeX_keys = []
	num_of_bibtex_entries = 0
	# ============================================================
	#	Other methods.
	# ============================================================
	#	Method to add BibTeX keys into a list, "set_of_BibTeX_keys".
	#	O(n) method, where n is the number of BibTeX keys.
	@staticmethod
	def add_BibTeX_key(found_BibTeX_key):
		if (found_BibTeX_key in Typeset_to_LaTeX.set_of_BibTeX_keys):
			temp_str = "Duplicate BibTeX key:"+found_BibTeX_key
			warnings.warn(temp_str)
			raise Exception("Multiple instances of a BibTeX key")
		Typeset_to_LaTeX.set_of_BibTeX_keys.append(found_BibTeX_key)
	# ============================================================
	#	Method to sort BibTeX keys into a list, "set_of_BibTeX_keys".
	#	O(n*log(n)) method, where n is the number of BibTeX keys.
	@staticmethod
	def sort_BibTeX_keys():
		Typeset_to_LaTeX.set_of_BibTeX_keys = sorted(Typeset_to_LaTeX.set_of_BibTeX_keys)
	# ============================================================
	#	Method to read each line of the input BibTeX file/database.
	#		Parse each BibTeX entry in the BibTeX database.
	#		Add each unique BibTeX key to a set of BibTeX keys.
	#		For duplicate BibTeX keys that are found, report them
	#			as an error so that the duplicate BibTeX keys can
	#			be removed.
	#	O(n) method, where n is the number of lines of the BibTeX file.
	@staticmethod
	def process_input_BibTeX_file(ip_file_object,input_BibTeX_file):
		#print "--------------------------------------------------------"
		println = "=	Reading input BibTeX file:"
		println += input_BibTeX_file
		print(println)
		# Read each available line in the input BibTeX file.
		for line in ip_file_object:
			# Is this line the 1st line of a BibTeX entry?
			if "@" == line[0]:
				# Yes.
#				print "...	First line of a BibTeX entry."
				# Increment number of BibTeX entries.
				Typeset_to_LaTeX.num_of_bibtex_entries = Typeset_to_LaTeX.num_of_bibtex_entries + 1
				tokenized_BibTeX_entry = re.split('@|{|,',line)
#				for i in tokenized_BibTeX_entry:
#					print i
				# Is the type of the BibTeX entry valid?
				if (tokenized_BibTeX_entry[1] in queue_ip_args.BibTeX_entry_types):
					# Yes. Try adding the BibTeX entry to "set_of_BibTeX_keys".
					Typeset_to_LaTeX.add_BibTeX_key(tokenized_BibTeX_entry[2])
				else:
					# No. Warn user that the type of BibTeX entry is invalid!
					temp_str = "Invalid type of BibTeX entry:"
					temp_str += tokenized_BibTeX_entry[1]
					print(temp_str)
					#warnings.warn("Invalid type of BibTeX entry")
					raise Exception("BibTeX entry has an invalid type!")
		"""
			Postcondition: Check if the number of BibTeX entries
				in the BibTeX database match with the cardinality
				of the set of BibTeX entries.
		"""
		if (Typeset_to_LaTeX.num_of_bibtex_entries != len(Typeset_to_LaTeX.set_of_BibTeX_keys)):
			raise Exception("Mismatch in number of BibTeX entries processed.")
		else:
			print("=	Number of BibTeX entries processed: {}" .format(str(Typeset_to_LaTeX.num_of_bibtex_entries)))
	# ============================================================
	#	Method to print set of BibTeX keys to standard output.
	#	O(n) method, where n is the number of BibTeX keys to print.
	@staticmethod
	def print_BibTeX_keys():
		# Sort the BibTeX keys in lexicographical order.
		Typeset_to_LaTeX.sort_BibTeX_keys()
		# Print the BibTeX keys in lexicographical order.
		print(Typeset_to_LaTeX.set_of_BibTeX_keys)
	# ============================================================
	#	Method to print set of BibTeX keys to a LaTeX (insert) file.
	#	O(n) method, where n is the number of BibTeX keys to print.
	@staticmethod
	def print_BibTeX_keys_to_LaTeX():
		# Relative path to output file.
		#output_file_relative_path = "/Applications/apps/comune/scripts/bibtex-analytics/test-with-typesetting/all-bibtex-keys.tex"
		output_file_relative_path = "/Users/zhiyang/Documents/ricerca/saag-bibtex/test-with-typesetting/all-bibtex-keys.tex"
		# Create file object for output file.
		op_file_obj = file_io_operations.open_file_object_write(output_file_relative_path)
		# \cite{} command prefix
		cite_cmd_prefix = "\cite{"
		# \cite{} command postfix
		cite_cmd_postfix = "}"
		# Sort the BibTeX keys in lexicographical order.
		Typeset_to_LaTeX.sort_BibTeX_keys()
		"""
			Turn this huge list (about, if not more than 16300 references)
				into a list of 10-element list.
		"""
		"""
			Modulo size of lists; perform modulo operation on this number.
			list_size (modulo) sub_list_size
		"""
		sub_list_size = 10
		list_of_sublists = [Typeset_to_LaTeX.set_of_BibTeX_keys[i * sub_list_size:(i + 1) * sub_list_size] for i in range((len(Typeset_to_LaTeX.set_of_BibTeX_keys) + sub_list_size - 1) // sub_list_size )]
		"""
			For each sublist of BibTeX entries, concatenate the BibTeX keys
				into a string.
		"""
		comma_separator = ","
		for i in list_of_sublists:
			temp_concatenated_BibTeX_keys = comma_separator.join(i)
			temp_cite_cmd = cite_cmd_prefix + temp_concatenated_BibTeX_keys + cite_cmd_postfix
			# Print the BibTeX keys in lexicographical order.
			op_file_obj.write(temp_cite_cmd)
		"""
		concatenated_BibTeX_keys = comma_separator.join(Typeset_to_LaTeX.set_of_BibTeX_keys)
		final_cite_cmd = cite_cmd_prefix + concatenated_BibTeX_keys + cite_cmd_postfix
		"""
		# Print the BibTeX keys in lexicographical order.
		#op_file_obj.write(final_cite_cmd)
		# Close file object for output file.
		file_io_operations.close_file_object(op_file_obj)
		# Typeset the LaTeX document into a PDF file.
		#	The following command failed to work.
		subprocess.run(["make", "latex"])
		"""
			Instead of using a Makefile for build automation, use
				a sequence of LaTeX/BibTeX commands.
		subprocess.run(["pdflatex", "articolo"])
		subprocess.run(["bibtex", "articolo"])
		subprocess.run(["pdflatex", "articolo"])
		subprocess.run(["bibtex", "articolo"])
		subprocess.run(["pdflatex", "articolo"])
		"""









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
	print("Finding duplicate BibTeX entries in my BibTeX database.")
	print("	And, if they exist, warn the user about them.")
	print("")
	# Assign input arguments to "queue_ip_args" for processing.
	queue_ip_args.set_input_arguments(sys.argv,queue_ip_args.DUPLICATE_ENTRIES)
	# Check if user wants to read the brief user manual.
	queue_ip_args.check_if_help_wanted()
	# Process the first input argument.
	print("=	Process the first input argument.")
	ip_filename = queue_ip_args.process_1st_ip_arg()
	# Create a file object for reading.
	print("=	Create a file object for reading.")
	# Create a file object for input BibTeX file, in reading mode.
	ip_file_obj = file_io_operations.open_file_object_read(ip_filename)
	Typeset_to_LaTeX.process_input_BibTeX_file(ip_file_obj,ip_filename)
	# Print the BibTeX keys in lexicographical order to standard output.
	#Typeset_to_LaTeX.print_BibTeX_keys()
	# Print the BibTeX keys in lexicographical order to LaTeX.
	Typeset_to_LaTeX.print_BibTeX_keys_to_LaTeX()
	# Close the file object for reading.
	print("=	Close the file object for reading.")
	file_io_operations.close_file_object(ip_file_obj)
