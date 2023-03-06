#	Makefile for build automation.

#	This is written by Zhiyang Ong to run automated regression tests
#		automatically.

#	================================================================

#	The MIT License (MIT)

#	Copyright (c) <2014-2017> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?

#	================================================================

#	Make targets

all:
	@echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	@echo === Run automated regression testing.
	./automated_regression_testing.py
	@echo === Remove temp files.
	rm input/missing_doi_url_op.bib input/no_duplicate_bibtex_keys_op.bib input/y-dummy.bib
	rm input/one_bibtex_entry_clean.bib input/simple_clean.bib input/no_duplicate_bibtex_keys_clean.bib 



docs:
	pydoc -w keywords_display
	pydoc -w duplicate_BibTeX_entries
	pydoc -w incremental_test
	pydoc -w publishers
	pydoc -w rm_bibtex_metadata
	pydoc -w tutti_series
	pydoc -w validate_url
	pydoc -w automated_regression_testing



clean:
	rm -rf *.pyc
	rm -rf database/*.pyc
	rm -rf database/*.pyc
	rm -rf *.html
	rm input/*_op.bib







#	================================================================
#	Port scripts from Python 2.y to Python 3.x. 

duplicate:
	./duplicate_BibTeX_entries.py input/simple.bib
	./duplicate_BibTeX_entries.py input/simple_clean.bib
	./duplicate_BibTeX_entries.py input/one_bibtex_entry.bib
	./duplicate_BibTeX_entries.py input/one_bibtex_entry_clean.bib
	./duplicate_BibTeX_entries.py input/duplicates_bibtex_keys.bib

incre:
	./incremental_test.py input/simple.bib
	./incremental_test.py input/simple_clean.bib
	./incremental_test.py input/one_bibtex_entry.bib
	./incremental_test.py input/one_bibtex_entry_clean.bib
	

keywd:
	./keywords_display.py input/simple.bib
	./keywords_display.py input/simple_clean.bib
	./keywords_display.py input/one_bibtex_entry.bib
	./keywords_display.py input/one_bibtex_entry_clean.bib



pub:
	./publishers.py input/simple.bib
	./publishers.py input/simple_clean.bib
	./publishers.py input/one_bibtex_entry.bib
	./publishers.py input/one_bibtex_entry_clean.bib


meta:
	./rm_bibtex_metadata.py input/simple.bib
	./rm_bibtex_metadata.py input/simple_clean.bib
	./rm_bibtex_metadata.py input/one_bibtex_entry.bib
	./rm_bibtex_metadata.py input/one_bibtex_entry_clean.bib




partition:
	@echo "	Requires installation of pybtex: e.g., pip install pybtex."
	pybtex-format --style alpha input/t-simple.bib output-files/t-simple-alpha.md
	pybtex-format --style plain input/t-simple.bib output-files/t-simple-plain.md
	pybtex-format --style unsrt input/t-simple.bib output-files/t-simple-unsrt.md
	@echo "	The 'abbrv' style is not available for pybtex."
	#pybtex-format --style abbrv input/t-simple.bib output-files/t-simple-abbrv.md





series:
	./tutti_series.py input/simple.bib
	./tutti_series.py input/simple_clean.bib
	./tutti_series.py input/one_bibtex_entry.bib
	./tutti_series.py input/one_bibtex_entry_clean.bib

vald:
	./validate_url.py input/simple.bib
	./validate_url.py input/simple_clean.bib
	./validate_url.py input/one_bibtex_entry.bib
	./validate_url.py input/one_bibtex_entry_clean.bib









