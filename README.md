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

## Old notes about the organization of this repository.


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
+ ***extract_bibtex_entries.py***
	- Run as: **./extract_bibtex_entries.py [-h] [-k] [set of BibTeX keys stored as a CSV file] [-m] [set of keyphrases stored as a CSV file]**
		- For future version: **./extract_bibtex_entries.py [-h] [-k] [set of BibTeX keys stored as a CSV file] [-m] [set of keyphrases stored as a CSV file] [-a] [names of authors as a string] [-z] [names of authors as a string] [-b] [booktitle as a string] [-j] [journal title as a string] [-s] [book series as a string] [-u] [name of university as a string]**
	- A *Python* script to extract a subset of BibTeX entries
		from a BibTeX database, using a non-empty subset of the following:
		* a set of BibTeX keys
		* a set of keyphrases, stored as optional metadata for each BibTeX entry
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







#	Additional Resources



Alternatives for the *Python* package *bibtexparser* [Boulogne2022] [Boulogne2023b] [Boulogne2023a] and the script ***extract_bibtex_entries.py*** that are explored:
+ on March 4, 2023:
	- [Biblib](https://github.com/aclements/biblib)
		* Last build: December 20, 2013.
		* Author: Austin Clements.
	- Pybtex [Golovizin2022] [Golovizin2022a] [Golovizin2021a] [Golovizin2021]
		* Supposed to replace *BibTeX*, which is not what I am looking for.
		* ***pybtex-format*** feature/utility allows me to print the
			contents of a *BibTeX* database into a text file that is
			in a readable format.
			- Fails to include information about the publisher and its
				address in the output file for the BibTeX entry type
				*misc* [Kopka2004, \S12.2.1 The entry types, pp. 231].
			- It does not work for all default bibliographic styles [Kopka2004, \S12.1 The BibTeX program, pp. 228-229].
				* It works for the following, but not *abbrv*:
					+ plain
					+ unsrt
					+ alpha
		* Requires installation: e.g., pip install pybtex
		* To parse the BibTeX database for processing a set of BibTeX keys or keyphrases, I tried the solution from [ex4].
			+ [ex4] Eetu 'ex4' Salpaharju and Lennart, Answer to "How to use the biblib parser with a bibtex file stored in a pyhon variable?", Stack Exchange Inc., New York, NY, April 27, 2020. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/61459722/1531728 and https://stackoverflow.com/questions/61459634/how-to-use-the-biblib-parser-with-a-bibtex-file-stored-in-a-pyhon-variable/61459722#61459722; November 9, 2021 was the last accessed date.
				- Solution has a run-time error:
					* syntax error, from pybtex.scanner.TokenRequired.
	- [Bib2ML (aka. Bib2HTML)](https://ctan.org/pkg/bib2ml?lang=en)
		* Reference: Franck Dernoncourt, Answer to "Convert BibTex file to database entries using Python", Stack Exchange Inc., New York, NY, October 17, 2015. Available online from Stack Exchange Inc.: Stack Overflow: Questions at: https://stackoverflow.com/a/33182448/1531728 and https://stackoverflow.com/questions/9235853/convert-bibtex-file-to-database-entries-using-python/33182448#33182448; March 6, 2023 was the last accessed date.
		* Solution not attempted. Did not want to explore using *Perl* script to address the problem.








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










#	References



+ [Boulogne2022]
	- Francois Boulogne, Michael Weiss, and sciunto, "bibtexparser 1.4.0," Python Software Foundation, Beaverton, OR, September 23, 2022. Available online from *PyPI -- The Python Package Index: pew 1.4.0* at: https://pypi.org/project/bibtexparser/; February 25, 2023 was the last accessed date.
+ [Boulogne2023a]
	- Fran{\c{c}}ois Boulogne, Olivier Mangin, Lucas Verney, and other contributors, "Tutorial," Read the Docs, Inc., Portland, OR, January 3, 2023. Available online from *Read the Docs: Welcome to BibtexParser's documentation!: Tutorial* as Version 1.4.0 at: https://bibtexparser.readthedocs.io/en/master/tutorial.html; February 25, 2023 was the last accessed date.
+ [Boulogne2023b]
	- Fran{\c{c}}ois Boulogne, Olivier Mangin, Lucas Verney, and other contributors, "bibtexparser: API," Read the Docs, Inc., Portland, OR, January 3, 2023. Available online from *Read the Docs: Welcome to BibtexParser's documentation!: bibtexparser: API* as Version 1.4.0 at: https://bibtexparser.readthedocs.io/en/master/bibtexparser.html; February 28, 2023 was the last accessed date.
+ [Golovizin2021a]
	- Andrey Golovizin and erosennin, "Pybtex 0.24.0: a BibTeX-compatible bibliography processor in Python", Python Software Foundation, Beaverton, OR, January 17 2021. Available online from *PyPI – The Python Package Index: pybtex 0.24.0* at: https://pypi\.org/project/pybtex/; March 5, 2023 was the last accessed date.
+ [Golovizin2021]
	- Andrey Golovizin, W. Trevor King, Matthias Troffaes, Jorrit Wronski, Hong, Jannik Schürg, Fabrice, David Chiang, Jerry James, Nathaniel Starkman, Tristan Stenner, Tomáš Hrnčiar, Jens Heinrich, Kunal Marwaha, and Julian Rüth, "Pybtex User's Guide", January 17 2021. Available online from *Pybtex!: docs: Pybtex User's Guide* as Version 0.24.0 at: https://docs.pybtex.org/; self-published; March 4, 2023 was the last accessed date.
+ [Golovizin2022]
	- Andrey Golovizin, W. Trevor King, Matthias Troffaes, Jorrit Wronski, Hong, Jannik Schürg, Fabrice, David Chiang, Jerry James, Nathaniel Starkman, Tristan Stenner, Tomáš Hrnčiar, Jens Heinrich, Kunal Marwaha, and Julian Rüth, "Pybtex!", 2022. Available online at: https://pybtex\.org/; self\-published; March 4, 2023 was the last accessed date.
+ [Golovizin2022a]
	- Andrey Golovizin, W. Trevor King, Matthias Troffaes, Jorrit Wronski, Hong, Jannik Schürg, Fabrice, David Chiang, Jerry James, Nathaniel Starkman, Tristan Stenner, Tomáš Hrnčiar, Jens Heinrich, Kunal Marwaha, and Julian Rüth, "Pybtex: a BibTeX\-compatible bibliography processor in Python", Atlassian Pty Ltd, Sydney, New South Wales, Australia, October 7 2022. Available online from *Bitbucket: Pybtex developers* at: https://bitbucket\.org/pybtex\-devs/pybtex and https://bitbucket\.org/pybtex\-devs/pybtex/src/master/; March 4, 2023 was the last accessed date.
+ [Kopka2004]
	- Helmut Kopka and Patrick W. Daly, "Guide to LaTeX," Fourth edition, in Addison-Wesley Series on Tools and Techniques for Computer Typesetting, Addison-Wesley, Boston, MA, 2004.





















#	Author Information

The MIT License (MIT)

Copyright (c) <2016> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.

