#	General Information

This set of scripts is to perform data analytics operations on my *BibTeX*
	database, and to clean it up.



My *BibTeX* database is a large set of *BibTeX* entries.
	Each *BibTeX* entry references a (research) publication.



[A report describing the organization of this repository and the software
	architecture of the *Python*-based software for *BibTeX Analytics*.](https://github.com/eda-ricercatore/bibtex-analytics/blob/master/notes/report/report.pdf)
+ It provides reference management of large *BibTeX* databases, including those
	that are greater than 20 MB or have more than 15 thousand *BibTeX* entries.
+ It performs data analytics on *BibTeX* entries in a given *BibTeX* database to
	detect emerging research trends and megatrends.




[A set of guidelines for potential and current collaborators.](https://github.com/eda-ricercatore/bibtex-analytics/blob/master/notes/guidelines/guidelines.pdf)


**Note that a test suite for incremental software testing [Insert references]** 
	


---

Old notes about the organization of this repository.


It contains the following scripts:
+ automated_regression_testing.py
	- Run as: **./automated_regression_testing.py**
	- No input nor output required.
	- A *Python* script to perform automated regression testing of the *Python* scripts for validating
		and cleaning *BibTeX* files, and *BibTeX* analytics.
	- **Sort of deprecated.** Still works though.
+ duplicate_BibTeX_entries.py
	- Run as: **./duplicate_BibTeX_entries.py [-h] [BibTeX file]**
	- A *Python* script to determine if duplicate BibTeX entries exist in my BibTeX
		database.
	- The script reports the existence of any non-standard BibTeX entry type
		that is found.
	- No output required.
	- IMPORTANT
+ editions.py
	- Run as: **./editions.py [input BibTeX file] [-h]**
	- A *Python* script to display a set of editions from *BibTeX* entries in a
		*BibTeX* database.
+ incremental_test.py
	- Run as: **./incremental_test.py [input BibTeX file]**
	- Perform incremental software testing automatically for my script(s) that
		perform data analytics operations with my BibTeX database.
	- **Debug how it handles zero input options/arguments.**
+ institutions.py
	- Run as: **./institutions.py [input BibTeX file] [-h]**
	- A *Python* script to display a set of institutions from *BibTeX* entries in a *BibTeX* file/database.
+ journal_titles.py
	- Run as: **./journal_titles.py [input BibTeX file] [-h]**
	- A *Python* script to display a set of journal titles from *BibTeX* entries in a *BibTeX* database.
+ keywords_display.py
	- Run as: **./keywords_display.py [input BibTeX file] [-h]**
	- A *Python* script to display a set of keywords/keyphrases from *BibTeX* entries in a BibTeX* database.
+ organizations.py
	- Run as: **./organizations.py [input BibTeX file] [-h]**
	- A *Python* script to display a set of organizations from *BibTeX* entries in a *BibTeX* database.
+ publishers.py
	- Run as: **./publishers.py [input BibTeX file] [-h]**
	- A *Python* script to display a set of publishers from *BibTeX* entries in a *BibTeX* database.
+ rm_bibtex_metadata.py
	- Run as: **./rm_bibtex_metadata.py [input BibTeX file] [output BibTeX file] [-h]**
	- *[output BibTeX file]* is an optional parameter.
	- A *Python* script to delint/remove *BibTeX* metadata from a *BibTeX* database/file.
+ tutti_series.py
	- Run as: **./tutti_series.py [input BibTeX file] [-h]**
	- A *Python* script to display series from *BibTeX* entries in a *BibTeX* database.
+ validate_url.py
	- Run as: **./validate_url.py [input BibTeX file] [output BibTeX file] [-h]**
	- Validate the URL field of BibTeX entries in my BibTeX database.
	- Validate the DOI field of BibTeX entries in my BibTeX database.
	- If there exists backup URL and there does not exist any URL/DOI
		entry, add URL/DOI entry.
	- No output required.
	- IMPORTANT
+ z_booktitles.py
	- Run as: **./z_booktitles.py [input BibTeX file] [-h]**
	- A *Python* script to display booktitles from all *BibTeX* entries in a *BibTeX* database.













#	*BibTeX* Benchmarks

This section describes the set of *BibTeX* benchmarks that I used to
	test various scripts for processing *BibTeX* databases. 

##	*BibTeX* Benchmarks for duplicate_BibTeX_entries.py

The set of *BibTeX* benchmarks that I have used to test
	*duplicate_BibTeX_entries.py* are:
+ one_bibtex_entry.bib
+ simple.bib
+ no_duplicate_bibtex_keys.bib


##	*BibTeX* Benchmarks for validate_url.py

The set of *BibTeX* benchmarks that I have used to test
	*validate_url.py* are:
+ has_backup2_no_backup1.bib
+ missing_doi_url.bib
+ no_duplicate_bibtex_keys.bib


##	*BibTeX* Benchmarks for rm_bibtex_metadata.py

The set of *BibTeX* benchmarks that I have used to test
	*rm_bibtex_metadata.py* are:
+ one_bibtex_entry.bib
+ simple.bib
+ no_duplicate_bibtex_keys.bib

This is the same set of *BibTeX* benchmarks that I have used to test
	*duplicate_BibTeX_entries.py*.


##	*BibTeX* Benchmarks for incremental_test.py

The set of *BibTeX* benchmarks that I have used to test
	*incremental_test.py* are:






#	Future Work

Complete the work on data analytics, including predictive analytics.


+ For a given keyphrase, provide a list of *BibTeX* entries that contain that
	keyphrase in their keyword *BibTeX* field.
+ Perform miscellaneous tasks to clean up the *BibTeX* file.
+ Check if the ampersand is surrounded by curly braces and set to the normal
	(non-Italics) font.
+ For each conference, check if its abbreviation is placed within
		round brackets after the title of the conference proceedings.
	  Check if there is no comma between the title and the
		abbreviation.
+ Write a script to extract the keywords from the *BibTeX*
		repository, arrange them in alphabetical order, and pipe them
		to an output file.
+ Check if the addresses of the publications have the U.S. states in capital letters.
	- If I use abbreviations for states and territories in Australia and Canada, do
		likewise.
	- For publications outside the U.S., (and Australia and Canada), ignore this.
+ Check if DOIs and/or URL fields are missing, if the following fields (metadata
	for *BibDesk*) exists:
	- "Bdsk-Url-1". 






I can develop *Python* scripts to do the following:
+ extract_citations.py
	- ./extract_citations.py [LaTeX sources] [BibTeX output]
	- Produces an intermediate output, which is a set of BibTeX keys
		that uniquely identifies a matching *BibTeX* entry in my *BibTeX*
		database.
+ not_defined_references.py
	- ./not_defined_references.py  [LaTeX sources] [BibTeX input]
	- Check if this citation uses a undefined reference
	- No output required.
+ uncomment_latex_src_files.py
	- ./uncomment_latex_src_files.py [dirty LaTeX source files] [clean LaTeX source files]
	- Remove comments from *LaTeX* source files. Non importante.




[See the report for an updated description of future work for the *BibTeX Analytics* project.](https://github.com/eda-ricercatore/bibtex-analytics/blob/master/notes/report/report.pdf)





#	Author Information

The MIT License (MIT)

Copyright (c) <2016> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.

