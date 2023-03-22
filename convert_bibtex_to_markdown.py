#!/Users/zhiyang/anaconda3/bin/python

#	#!/usr/local/bin/python3


"""
	This is written by Zhiyang Ong to extract a subset of BibTeX entries
		from a BibTeX database, using a non-empty subset of the following:
	+ a set of BibTeX keys
	+ a set of keyphrases, stored as optional metadata for each BibTeX entry



	Synopsis: command name and [argument(s)]
	./convert_bibtex_to_markdown.py [BibTeX database]
	


	Parameters:
	[input BibTeX file]:	A BibTeX database.

	




	Its procedure is described as follows:
	
	Process input arguments.
		If there is an input argument, assign it to the filename for
			a BibTeX database to be processed.
		If there are multiple input arguments, only process the first
			input argument as the filename for the BibTeX database to
			be processed.
		If there are no input arguments, use the default filename for
			the BibTeX database.
	Open a BibTeX database, and create an input file object for it.
	Create a file object for the output Markdown document.
	Parse the BibTeX database, via a BibTeX parser and the file object.
	For each entry in the BibTeX database,
		print it to an output Markdown document using the parenthetical
			referencing system with the author-date citation style.



		



	Notes/Assumptions:
	Since the installation of packages via PyPI are placed in the Anaconda
		"Conda" environment, and my Python environment is dependent on the
		"Conda" package and environment management system, I have to use
		the Python interpreter from Conda to use the PyPI package installations.
	Else, I can use other Python interpreters, one of which is commented out
		to enable the usage of the Python interpreter from Conda.
	Run this in the ./outputs/ subdirectory of the BibTeX database repository.
	




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
	+ [MendeleyLimitedStaff2022b]
		- Mendeley Limited staff, "Ultimate Citation Cheat Sheet," Mendeley Limited, London, U.K., 2022. Available online from *Welcome to Mendeley: Support: Help Guides: Guides: Help guides: Citation Guides: Citation Hub: Contents: Ultimate Citation Cheat Sheet* at: https://www.mendeley.com/guides/ultimate-citation-cheat-sheet/; March 7, 2023 was the last accessed date.
	+ [MendeleyLimitedStaff2022a]
		- Mendeley Limited staff, "Harvard Format Citation Guide," Mendeley Limited, London, U.K., 2022. Available online from *Welcome to Mendeley: Support: Help Guides: Guides: Help guides: Citation Guides: Citation Hub: Harvard* at: https://www.mendeley.com/guides/harvard-citation-guide/; March 7, 2023 was the last accessed date.
	+ [Turabian2018]
		- Kate L. Turabian, Wayne C. Booth, Gregory G. Colomb, Joseph M. Williams, Joseph Bizup, William T. FitzGerald, and The University of Chicago Press Editorial Staff, "A Manual for Writers of Research Papers, Theses, and Dissertations: Chicago Style for Students and Researchers," Ninth edition, Chicago Guides to Writing, Editing, and Publishing series, The University of Chicago Press, Chicago, IL and London, U.K., 2018. DOI: https://dx.doi.org/10.7208/chicago/9780226430607.001.0001.
	+ [Turabian2007]
		- Kate L. Turabian, Wayne C. Booth, Gregory G. Colomb, Joseph M. Williams, and The University of Chicago Press Editorial Staff, "A Manual for Writers of Research Papers, Theses, and Dissertations: Chicago Style for Students and Researchers," Seventh edition, Chicago Guides to Writing, Editing, and Publishing series, The University of Chicago Press, Chicago, IL and London, U.K., 2007.
	+ [WikipediaContributors2023e]
		- Wikipedia contributors, "Citation," Wikimedia Foundation, San Francisco, CA, February 25, 2023. Available online from *Wikipedia, The Free Encyclopedia: Bibliography* at: https://en.wikipedia.org/wiki/Citation; March 7, 2023 was the last accessed date.
	+ [WikipediaContributors2023d]
		- Wikipedia contributors, "Parenthetical referencing," Wikimedia Foundation, San Francisco, CA, January 11, 2023. Available online from *Wikipedia, The Free Encyclopedia: Style guides* at: https://en.wikipedia.org/wiki/Parenthetical_referencing; March 7, 2023 was the last accessed date.







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




# Filename/path to the BibTeX database that would be parsed and processed.
input_bibtex_file = "./input-files/bibtext_entries_for_cpp.bib"

"""
	Filename/path of the output file that contains the extracted
		BibTeX entries.
"""
output_filename = "./output-files/references_in_markdown.md"

# Error flags for sys.exit() method calls.
# Input filename is invalid.
input_filename_is_invalid = 1
# Output filename, or path of output file, is invalid.
output_filename_or_path_is_invalid = 2




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
	print("Synopsis of using: convert_bibtex_to_markdown.py")
	print("")
	print("./convert_bibtex_to_markdown.py [input BibTeX database]")
	print("")




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
	Method to format the list of authors names correctly.
	@param list_of_authors - A string containing the list of names
		of author(s).
	@return a string containing the list of names of author(s)
		that are comma separated, rather than by " and ";
		if list_of_authors refers to a None object, return an
			empty string.
"""
def process_author_field(list_of_authors=None):
	# Is the list of author names not a None object?
	if list_of_authors is not None:
		# Yes. Delimit the names of the authors by " and ".
		list_of_authors_delimited = list_of_authors.split(" and ")
		# Final list of names of authors.
		list_of_authors_final = ""
		for index, name in enumerate(list_of_authors_delimited):
			if 0 == index:
				list_of_authors_final = name
			elif ((len(list_of_authors_delimited) - 1) == index):
				list_of_authors_final = list_of_authors_final + ", and " + name
			else:
				list_of_authors_final = list_of_authors_final + ", " + name
		return list_of_authors_final
	else:
		# No, it is a None object. Return an empty string.
		return ""






"""
	Method to format how the 'Howpublished' field is italicized.
	@param howpublished_field - string containing information for
		the 'Howpublished' field.
	@param markdown_italicization - boolean flag that indicates
		if the 'Howpublished' field should be italicized in
		Markdown format or remain in LaTeX format.
	@return a string containing the 'Howpublished' field that is
		italicized in the format specified by the boolean flag,
		'markdown_italicization'.
"""
def process_howpublished_field(howpublished_field="", markdown_italicization=True):
	# boolean flag for LaTeX italicization.
	latex_italicization = False
	"""
		Should the 'Howpublished' field should be italicized in
			Markdown format?
	"""
	if markdown_italicization:
		# Yes. Change the italicization format from LaTeX to Markdown.
		# Replace "} as Version" substring to "* as Version".
		howpublished_field_for_markdown = howpublished_field.replace("} as Version","* as Version")
		# Replace "} and {\it " substring to "* and *".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("} and {\it ","* and *")
		# Replace "}, and {\it " substring to "*, and *".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("}, and {\it ","*, and *")
		# Replace "} via {\it " substring to "* via *".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("} via {\it ","* via *")
		# Is there any remaining LaTeX italicization in the string?
		if " {\it " in howpublished_field_for_markdown:
			# Set boolean flag for LaTeX italicization to be true.
			latex_italicization = True
		# Replace "{\it " substring to "*".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("{\it ","*")
		# Replace "} as " substring to "* as ".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("} as "," as ")
		# Replace "}, at: \url{" substring to "*, at: ".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("}, at: \\url{","*, at: ")
		# Replace "} at: \url{" substring to "* at: ".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("} at: \\url{","* at: ")
		# Replace " at: \url{" substring to "* at: ".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace(" at: \\url{"," at: ")
		# Replace "}, \url{" substring to ", ".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("}, \\url{",", ")
		# Replace "} and \url{" substring to " and ".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("} and \\url{"," and ")
		# Replace "}, and \url{" substring to ", and ".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("}, and \\url{",", and ")
		# Replace "}; " substring to "; ".
		howpublished_field_for_markdown = howpublished_field_for_markdown.replace("}; ","; ")
		"""
			Replace "}, " substring to "*, ".

			This can resolve some bugs, but also introduces other bugs.
			
			This is because there are instances of "}, " that should
				be replaced, but not in other instances.
		"""
		#howpublished_field_for_markdown = howpublished_field_for_markdown.replace("}, ","*, ")
		# Add a period to the modified 'Howpublished' field.
		howpublished_field_for_markdown = howpublished_field_for_markdown + "."
		# Does the string contain the start of italicization in LaTeX.
		#if " {\it " in howpublished_field_for_markdown:
		if latex_italicization:
			# Yes. Replace "}." substring to "*.".
			howpublished_field_for_markdown = howpublished_field_for_markdown.replace("}.","*.")
		# Else, append a period to the end of the 'Howpublished' field.
		# Return the modified 'Howpublished' field in Markdown format.
		return howpublished_field_for_markdown
	else:
		# No. Return string for 'Howpublished' field without modification.
		return howpublished_field







###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	#	= Set up loading of BibTeX database
	# Type of current time measurement.
	mode_current_time_measurement = "perf_counter"
	# Set the initial timestamp.
	execution_time_measurement_no_ns.set_initial_timestamp()
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
		else:
			output_filename = sys.argv[1]
	else:
		"""
			No, check if the name of the input BibTeX database/file
				is not empty or None.
		"""
		if input_bibtex_file == None:
			# Print the help manual.
			print_help_manual()
			# End execution of the script with an error.
			sys.exit(input_filename_is_invalid)
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
		Create input and output file streams to load the BibTeX database
			as an input file object for the parser [Boulogne2023a], and
			to write to the designated/default output file.

		Run this in the ./outputs/ subdirectory of the BibTeX
			database repository.
	"""
	with open(input_bibtex_file, "r") as ip_file_1, open(output_filename, "w") as op_file_1:
		# Print the preamble for the Mardown document of references.
		op_file_1.write("#	References\n")
		op_file_1.write("\n")
		# Load the BibTeX database to the parser.
		bib_database = bibtexparser.load(ip_file_1)
		"""
			Enumerate the list of BibTeX entries, and print them to
				the output file in Markdown format, using the
				author-date method (or Harvard referencing style
				or Harvard citation style) for parenthetical referencing.
			[MendeleyLimitedStaff2022b] [MendeleyLimitedStaff2022a] [Turabian2018] [Turabian2007] [WikipediaContributors2023e] [WikipediaContributors2023d]

			Author(s)/Editor(s), "Title," Edition, Series, Volume, Number, Pages, Publisher/Institution or Organization [for manuals], Address, Month, Year.
			Howpublished [field]. URL (if Howpublished is not available). DOI.

			Author(s)/Editor(s), "Title," Chapter, Booktitle, Edition, Series, Volume, Number, Pages, Publisher, Address, Month, Year.
			Howpublished [field]. URL (if Howpublished is not available). DOI.

			Author(s)/Editor(s), "Title," Journal, Volume, Number, Pages, Publisher, Address, Month, Year.
			Howpublished [field]. URL (if Howpublished is not available). DOI.

			Author(s)/Editor(s), "Title," Number, School, Address, Month, Year.
			Howpublished [field]. URL (if Howpublished is not available). DOI.

			Author(s)/Editor(s), "Title," Publisher/School, Address, Month, Year.
			Howpublished [field]. URL (if Howpublished is not available). DOI.

			####TO BE COMPLETED
		"""
		for bib_entry in bib_database.entries:
			current_string_being_processed = "+ ["
			current_publication = "	- "
			"""
				'ENTRYTYPE' indicates the type of BibTeX entry, or
					BibTeX entry type.

				Print the BibTeX key.
			"""
			# Does this BibTeX entry has the BibTeX field "ID"?
			if bib_entry.get("ID") is not None:
				# Yes, if the ID field not empty?
				if "" != bib_entry.get("ID"):
					# Yes, append ID to information about the publication.
					current_string_being_processed = current_string_being_processed + bib_entry.get("ID") + "]\n"
					op_file_1.write(current_string_being_processed)
					current_string_being_processed = ""
			# Does this BibTeX entry has the BibTeX field "author"?
			if bib_entry.get("author") is not None:
				# Yes, if the author field not empty?
				if "" != bib_entry.get("author"):
					# Yes, append names of authors to information about the publication.
					current_string_being_processed = bib_entry.get("author")
					current_publication = "	- " + process_author_field(current_string_being_processed)
			# Does this BibTeX entry has the BibTeX field "title"?
			if bib_entry.get("title") is not None:
				# Yes, if the title field not empty?
				if "" != bib_entry.get("title"):
					# Yes, append title to information about the publication.
					current_publication = current_publication + ", \"" + bib_entry.get("title") + "\""
			# Does this BibTeX entry has the BibTeX field "chapter"?
			if bib_entry.get("chapter") is not None:
				# Yes, if the chapter field not empty?
				if "" != bib_entry.get("chapter"):
					# Yes, append chapter to information about the publication.
					current_publication = current_publication + ", Chapter " + bib_entry.get("chapter")
			# Does this BibTeX entry has the BibTeX field "booktitle"?
			if bib_entry.get("booktitle") is not None:
				# Yes, if the booktitle field not empty?
				if "" != bib_entry.get("booktitle"):
					# Yes, append booktitle to information about the publication.
					current_publication = current_publication + ", *" + bib_entry.get("booktitle") + "*"
			# Does this BibTeX entry has the BibTeX field "edition"?
			if bib_entry.get("edition") is not None:
				# Yes, if the edition field not empty?
				if "" != bib_entry.get("edition"):
					# Yes, append edition to information about the publication.
					current_publication = current_publication + ", " + bib_entry.get("edition") + " edition"
			# Does this BibTeX entry has the BibTeX field "series"?
			if bib_entry.get("series") is not None:
				# Yes, if the series field not empty?
				if "" != bib_entry.get("series"):
					# Yes, append series to information about the publication.
					current_publication = current_publication + ", " + bib_entry.get("series") + " series"
			# Does this BibTeX entry has the BibTeX field "journal"?
			if bib_entry.get("journal") is not None:
				# Yes, if the journal field not empty?
				if "" != bib_entry.get("journal"):
					# Yes, append journal to information about the publication.
					current_publication = current_publication + ", *" + bib_entry.get("journal") + "*"
			# Does this BibTeX entry has the BibTeX field "volume"?
			if bib_entry.get("volume") is not None:
				# Yes, if the volume field not empty?
				if "" != bib_entry.get("volume"):
					# Yes, append volume to information about the publication.
					current_publication = current_publication + ", Volume " + bib_entry.get("volume")
			# Does this BibTeX entry has the BibTeX field "number"?
			if bib_entry.get("number") is not None:
				# Yes, if the number field not empty?
				if "" != bib_entry.get("number"):
					# Yes, append the number to information about the publication.
					current_publication = current_publication + ", Number " + bib_entry.get("number")
			# Does this BibTeX entry has the BibTeX field "pages"?
			if bib_entry.get("pages") is not None:
				# Yes, if the pages field not empty?
				if "" != bib_entry.get("pages"):
					# Yes, append the pages to information about the publication.
					current_publication = current_publication + ", pp. " + bib_entry.get("pages")
			"""
				Does this BibTeX entry has the BibTeX field "publisher"?
				Publisher/Institution or Organization [for manuals]
				School
			"""
			if bib_entry.get("publisher") is not None:
				# Yes, if the publisher field not empty?
				if "" != bib_entry.get("publisher"):
					# Yes, append the publisher to information about the publication.
					current_publication = current_publication + ", " + bib_entry.get("publisher")
			# Does this BibTeX entry has the BibTeX field "address"?
			if bib_entry.get("address") is not None:
				# Yes, if the address field not empty?
				if "" != bib_entry.get("address"):
					# Yes, append the address to information about the publication.
					current_publication = current_publication + ", " + bib_entry.get("address")
			# Does this BibTeX entry has the BibTeX field "month"?
			if bib_entry.get("month") is not None:
				# Yes, if the month field not empty?
				if "" != bib_entry.get("month"):
					# Yes, append the month to information about the publication.
					current_publication = current_publication + ", " + bib_entry.get("month")
			# Does this BibTeX entry has the BibTeX field "year"?
			if bib_entry.get("year") is not None:
				# Yes, if the year field not empty?
				if "" != bib_entry.get("year"):
					# Yes, append the year to information about the publication.
					current_publication = current_publication + ", " + bib_entry.get("year") + "."
			# Does this BibTeX entry has the BibTeX field "howpublished"?
			if bib_entry.get("howpublished") is not None:
				# Yes, if the howpublished field not empty?
				if "" != bib_entry.get("howpublished"):
					# Yes, append the howpublished to information about the publication.
					current_string_being_processed = process_howpublished_field(bib_entry.get("howpublished"))
					current_publication = current_publication + " " + current_string_being_processed
			# Does this BibTeX entry has the BibTeX field "doi"?
			if bib_entry.get("doi") is not None:
				# Yes, if the doi field not empty?
				if "" != bib_entry.get("doi"):
					# Yes, append the doi to information about the publication.
					current_publication = current_publication + ". DOI: " + bib_entry.get("doi") + "."
			# Write the information of the current publication to file.
			current_publication = current_publication + "\n"
			op_file_1.write(current_publication)
		"""
			Print the set of remaining BibTeX entries with the selected
				BibTeX keys.
		"""
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