#!/usr/local/bin/python3

"""
	This is written by Zhiyang Ong to check if a file is in the binary
		or text format.

	If it is supposed to be in the text format, find the binary characters.



	Replace this with the UNIX/macOS command:
	file -e ascii FILENAME

	If this command and the specified options return "data", it is a
		text file, rather than a binary file.




	References:

	Citations/references that use the LaTeX/BibTeX notation are taken from my BibTeX database
		(set of BibTeX entries).

	If these citations are not found in this list of references, information about them can be found in my BibTeX database.

	+ 


"""


"""
import mimetypes

mime = mimetypes.guess_type("../../references.bib")

print("mime is:",mime,"=")
"""


#is_binary_string(open("../../references.bib","rb")).read((1024))

#with open("../../references.bib","r",encoding="utf-8") as file_obj:
"""
with open("../references.bib","r",encoding="utf-8") as file_obj:
	# print("File is text, not binary.")
	for line in file_obj:
		print(line)


try:
	with open("../references.bib","r") as file_obj:
		# print("File is text, not binary.")
		for line in file_obj:
			print(line)
except UnicodeDecodeError:
	print("WHat??? What happened???")
"""

#pip install binaryornot


from binaryornot.check import is_binary
is_binary("../references.bib")