#!/usr/bin/python -m timeit -s

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


	This method of performance measurement based on using the timeit
		does not work.

	Assumptions:
		BibTeX keys are 


	Dedicated to a racist clown at Texas A&M University, who described
		me with ethnic/racial slurs.
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
"""
	Module for measuring performance (based on execution time)
		\cite{Ivan2014}.
"""
import timeit


#	Measure performance (based on execution time) \cite{Ivan2014}.

"""
	The following block of code does not work.

	num = 5

	def foobar(x):
		return x + 1

	print "	Performance based on timeit:",timeit.timeit(foobar(num)),"."
"""


start_time = timeit.default_timer()
a = 5^3
print "	Processed time:",timeit.default_timer() - start_time
























