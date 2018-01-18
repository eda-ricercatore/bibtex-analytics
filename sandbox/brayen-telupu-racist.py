#!/usr/bin/python

"""
	This Python script is written by Zhiyang Ong to test concepts
		in caseless string comparisons of BibTeX entries.

	Synopsis:
	Compare BibTeX keys in my BibTeX database, and indicate if they
		are the same.

	This script can be executed as follows:
	./brayen-telupu-racist.py

	Parameters:
	[]:			No input parameters.


	Assumptions:
		BibTeX keys are 


	Dedicated to racist folx at the Cru chapter at Texas A&M
		University, including the lead Cru staff "Brayen Telupu".
	Shout out to y'all for the extra motivation to graduate with my
		EECS Ph.D. in a small number of finte delta time steps!




	Revision History:
	August 15, 2017		Version 0.1. Initial build.
"""


__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'Aug 15, 2017'

#	The MIT License (MIT)

#	Copyright (c) <2014-2017> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?




#	Import modules from the Python Standard Library.
#	Module for using regular expression.
import re
#	Module for using iterators to enumerate lists.
import itertools
#	Module for measuring process time and wall time.
import time
"""
	Module for measuring performance (based on execution time)
		\cite{Ivan2014}.
"""
import timeit
#	Module to use functions for performance measurement.
from datetime import datetime









"""
	Two examples of BibTeX keys, to test if my scripts for processing
		BibTeX entries would recognize BibTeX keys with different
		cases to be the same.
"""
racist_Brayen				= "Fotsy2017"
brayen_kkk					= "FotSy2017"
#	List of string[s]. Test list-based string comparison methods.
list_brayen_alt_right		= [brayen_kkk]
#list_brayen_alt_right[0]	= "FotSy2017"


"""
	Note that cumbersome methods for case-insensitive string
		comparison are avoided, so that I can keep the scripts
		(fairly) simple and easy to maintain.
"""

print "========================================================"
print ""

#print "--------------------------------------------------------"
print "Method 1. \cite{Shiwangi2016}"
"""
	This method for case-insensitive string comparison does not work
		well with unicode characters.

	Techniques for measuring Process time and Wall time.
	\cite{Mohtashim2017}
	
	time.clock() returns elapsed time based on number of
		clock cycles \cite{Ivan2014}.
"""
process_time = time.clock()
if re.search(racist_Brayen, brayen_kkk, re.IGNORECASE):
	print "	BibTeX keys with non-uniform cases:	Match."
else:
	print "	BibTeX keys with non-uniform cases:	Don't Match."
print "=	Process time:", time.clock() - process_time,"\b."





print "--------------------------------------------------------"
print "Method 2. \cite{Holcombe2008}"
"""
	May not necessarily work for non-English characters.

	Techniques for measuring Process time and Wall time.
	\cite{Mohtashim2017}
	
	time.time() returns actual time taken \cite{Ivan2014}.
"""
wall_time = time.time()
if racist_Brayen.lower() == brayen_kkk.lower():
	print "	BibTeX keys with non-uniform cases:	Match."
else:
	print "	BibTeX keys with non-uniform cases:	Don't Match."
print "=	Wall time:", time.time() - wall_time,"\b."




print "--------------------------------------------------------"
print "Method 3. \cite{Smith2014b}"
"""
	This solution is computationally expensive, due to the use of
		regular expressions, compared to the use of reducing the
		strings to a common case (either upper or lower case).

	Use datetime module for performance measurement of long tasks
		\cite{Ivan2014}.
"""
measurement_begin = datetime.now()
if re.match(racist_Brayen,brayen_kkk, flags=re.I):	# re.I == re.IGNORECASE
	print "	BibTeX keys with non-uniform cases:	Match."
else:
	print "	BibTeX keys with non-uniform cases:	Don't Match."
time_taken = datetime.now() - measurement_begin
print "	The time taken is:",time_taken,"\b." 


print "--------------------------------------------------------"
print "Method 4. \cite{Reese2010}"
"""
	Use datetime module for performance measurement
		\cite{DrakeJr2016e}.
"""
start_time = timeit.default_timer()
racist_Brayen_blanco = re.compile(racist_Brayen, flags=re.I)
if any(itertools.ifilter(racist_Brayen_blanco.match, list_brayen_alt_right)):
	print "	BibTeX keys with non-uniform cases:	Match."
else:
	print "	BibTeX keys with non-uniform cases:	Don't Match."
print "	Processed time:",timeit.default_timer() - start_time







print "--------------------------------------------------------"
print "Method 5. \cite{Reese2010}"
"""
	Use datetime module for performance measurement
		\cite{DrakeJr2016e}.
"""
racist_Brayen_blanco = re.compile(racist_Brayen, flags=re.I)
if filter(racist_Brayen_blanco.match, list_brayen_alt_right):
	print "	BibTeX keys with non-uniform cases:	Match."
else:
	print "	BibTeX keys with non-uniform cases:	Don't Match."


















"""
	Choose method 2, which is faster than the rest.


	Alternate methods for case-insensitive string comparison:
	+ \cite{Veedrac2015}, for Python 3, using casefold() or casefold,
		followed by 'unicodedata.normalize'.

	Alternate methods for measuring performance (based on execution
		time):
	+ \cite{Ivan2014}
		- import timeit
	+ Using performance profilers for software \cite{DrakeJr2016e}.
		- https://docs.python.org/2/library/profile.html
		- http://pypy.org/performance.html
		- https://www.ploggingdev.com/2016/12/performance-measurement-in-python-3/
		- http://uwpce-pythoncert.github.io/SystemDevelopment/profiling.html
		- https://www.huyng.com/posts/python-performance-analysis
"""







