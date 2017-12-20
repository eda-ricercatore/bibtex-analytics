#!/usr/bin/python
###	#!/usr/bin/python -mtimeit


"""
	This Python script is written by Zhiyang Ong to read my BibTeX
		database and construct a container of "entry" objects, each
		of which represents a BibTeX entry.
	That is, map each entry in my BibTeX database to an instance of
		the "entry" class, and add these instances to my/the
		collection of "entry" objects.
	
	Synopsis:
	Build a collection of "entry" objects, using my BibTeX database.

	This script can be executed as follows:
	./bibtex_database.py [input BibTeX file]

	Parameters:
	[input BibTeX file]:	A BibTeX file that may have duplicate
								BibTeX entries.




	Revision History:
	??????, 2014		Version 0.1
	March 14, 2017		Version 0.2	Testing the first argument.
	March 22, 2017		Version 0.3	Working on second argument.
	April 7, 2017		Version 0.4	Refactored script.
	April 14, 2017		Version 1.0 Working script release.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'Apr 14, 2017'

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

	pathlib->Path
				For mapping a string to a path. 
"""

import sys
import os
import os.path
#from pathlib import Path
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

















