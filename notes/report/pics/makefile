#	This Makefile is written by Zhiyang Ong for build automation compiling images for his report.

#	The MIT License (MIT)

#	Copyright (c) <2017> Zhiyang Ong

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.

# @author Zhiyang Ong

# =============================================================

# Definition of macro flags...

#	Location of the program "PlantUML."
PLANTUML=		/Applications/apps/graphics/plantuml/plantuml.1.2018.6.jar
#	PlantUML options.
PDF=			-tpdf
EPS=			-teps



#	Source files for "PlantUML."
SOURCE=			*.uml


#	EPS files.
EPSFILES=		*.eps
#	PDF files.
PDFFILES=		*.pdf




#	Java compiler and its options/flags, and Java Virtual Machine.
JAVA=			java
JAR=			-jar



#	UNIX-like processes/commands.
#	Convert an Encapsulated PostScript (EPS) file into a PDF file.
EPS2PDF=		epstopdf
#	Open files by using the default application associated with them.
OPEN=			open
#	Delete files and directories recursively
REMOVE=			rm -rf





# =============================================================
#	Compile.
all:
	asy -f pdf sw-arch.asy
	open *.pdf



# =============================================================
#	Get the version of "PlantUML".
try:
	$(JAVA)	$(JAR)	$(PLANTUML)	-version


# =============================================================
#	Remove temporary files.
clean:




#	java -jar plantuml.1.2018.6.jar -tpdf sw-arch.uml
#	java -jar plantuml.jar -tpdf sw-arch.uml
# =============================================================
#	Generate the PDF image of the software architecture.
arch:
	$(JAVA)	$(JAR)	$(PLANTUML)	$(SOURCE)	$(EPS)
	$(EPS2PDF)	$(EPSFILES)
	$(OPEN)	$(PDFFILES)
	$(REMOVE)	$(EPSFILES)


















