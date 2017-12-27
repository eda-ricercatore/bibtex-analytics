#!/usr/bin/python
###	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3


"""
	This Python script is written by Zhiyang Ong to map each BibTeX
		in my BibTeX database into an instance of the "bibtex_entry"
		class.


	Synopsis:
	Instantiate the "entry" class for a BibTeX entry in my BibTeX
		database.






	Notes/Assumptions:
	Each field of a BibTeX entry is usually contained in a line, and
		it represents a property of the "bibtex_entry" class.
	
	The only BibTeX fields that stores information in multiple lines
		are:
		* Annote
		* Note???
		* Abstract
		

	A field in a BibTeX entry is either listed or not mentioned.
		That is, duplicates of any given field should not exist in a
			BibTeX entry.
		If such duplicates exist, raise an exception an inform the
			user that the BibTeX database does not conform to the
			this assumption (based on Zhiyang Ong's preferred BibTeX
			syntax). 


	Revision History:
	December 19, 2017			Version 0.1, initial build.
"""




__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'December 19, 2017'

#	The MIT License (MIT)

#	Copyright (c) <2014-2017> <Zhiyang Ong>

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

	collections -> namedtuple
				To use named tuples.
	operator -> attrgetter
				To manipulate attributes of a named tuple as callable
					objects.
"""

#import sys
#import os
#import os.path
#from subprocess import call
#import time
import warnings
#import re
#from collections import namedtuple
#from operator import attrgetter

###############################################################
#	Import Custom Python Modules


###############################################################
"""
	Module that maps each BibTeX entry in my BibTeX database
		into an instance of the "bibtex_entry" class.
	with methods that check the validity of a BibTeX key.

	As each line in a BibTeX entry is parsed, check if it
		complies with the standard BibTeX syntax.

	Map each field, usually contained in a line, of a BibTeX
		entry into a property of the "bibtex_entry" class.

	Each field in a BibTeX entry shall be unique;
		that is, no duplicates for a given BibTeX field shall
			exist.
"""  
class bibtex_entry:




















"""
	Do I provide a function to parse each line the same way?
	I have parsed the following BibTeX fields differently.
	*	BibTeX key
	*	Keywords
	*	Publisher
	*	Series
	
	Yes.
	
	That said, only the following have to be tokenized.
	*	Author: Names of co-authors are separated by " and ".
	*	
	
	The address and publisher fields are separated by " and ".
		However, " and " is a subset of the name for some
			publishers.
		Hence, I would not bother to process the publisher
			BibTeX field for joint publishers.
		Springer is the only publisher that has many variations
			of its name.
		To the best of my knowledge, apart from some universities
			with associated publishers (or university presses),
			ACM and IEEE are the only publishers with associated
			publishers (ACM Press and IEEE Press). 
"""
