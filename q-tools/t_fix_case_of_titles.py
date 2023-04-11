#!/usr/local/bin/python3

"""
	This is written by Zhiyang Ong to convert a list of names for the "Author" or "Editor" fields in BibTeX into the proper letter case.

	A number of Web pages, digital libraries, and publications tend to list the titles of publications in upper case (or capitals). Hence, we need to fix the letter case for these titles before entering them into a reference management software, such as BibTeX databases.

	
	#### TO BE FIXED
	
	+ Bug #1
		- When titles have hyphens in them, the second hyphenated term
			starts with a lower seletterca insted of an upper ase letter.
		- E.g., The Politics Of The Non-partisan League




















	References:

	Citations/references that use the LaTeX/BibTeX notation are taken from my BibTeX database
		(set of BibTeX entries).

	If these citations are not found in this list of references, information about them can be found in my BibTeX database.

	+ 


"""


"""
new_phrase = "meta-heuristics is not capitalized".capitalize()
print(f"New phrase is:{new_phrase}=")
# Result is: Meta-heuristics is not capitalized
"""


#	A sample list of names from \cite{Jordan2013}.
title_all_uppercase = "METAHEURISTICS: FROM DESIGN TO IMPLEMENTATION"

title_all_uppercase = "LEARNING FROM DATA MADE EASY WITH R"
title_all_uppercase = "DATA ANALYSIS FROM SCRATCH WITH PYTHON"
title_all_uppercase = "SPECS: SIMULATION PROGRAM FOR ELECTRONIC CIRCUITS AND SYSTEMS"
title_all_uppercase = "CORPORATE AMERICA IS AT A CRITICAL CROSSROADS"
title_all_uppercase = "NEUROBONKERS"
title_all_uppercase = "FEATURED ARTICLES"
title_all_uppercase = "PUBLICATIONS AVAILABLE ON-LINE"
title_all_uppercase = "STANFORD VLSI RESEARCH GROUP"
title_all_uppercase = "SOCIETY CENTERED DESIGN"
title_all_uppercase = "REIMAGINE PUBLIC VALUE"
title_all_uppercase = "DESIGN FOR PEOPLE'S RIGHTS"
title_all_uppercase = "ENSURE FAIR AND JUST OVERSIGHT"
title_all_uppercase = "RE­DISTRIBUTE THE POWER OF TECHNOLOGY"
title_all_uppercase = "CREATE COMPASSION AT SCALE"
title_all_uppercase = "DESIGN FOR REGENERATIVE ACTION"
title_all_uppercase = "CONFRONT UNCERTAINTY"
title_all_uppercase = "THE DESIGN OF TREE AND TRELLIS DATA COMPRESSION SYSTEMS"
title_all_uppercase = "A COMPILER GENERATOR FOR SEMANTIC GRAMMARS"
title_all_uppercase = "INJECTIVE MODULES WITH FINITELY GENERATED ESSENTIAL SOCLE"
title_all_uppercase = "SOVIET THREATS TO INTERVENE IN THE MIDDLE EAST, 1956-1973"
title_all_uppercase = "THE POLITICS OF THE NON-PARTISAN LEAGUE"
	#	The Politics Of The Non-partisan League
title_all_uppercase = "THE OPTIMIZATION OF HORIZONTAL MICROCODE WITHIN AND BEYOND BASIC BLOCKS: AN APPLICATION OF PROCESSOR SCHEDULING WITH RESOURCES"
title_all_uppercase = "THE MATHEMATICAL STRUCTURE OF THE HUMAN SLEEP-WAKE CYCLE (CIRCADIAN, RHYTHM, MODELS, DYNAMICS, FREE-RUN)"
title_all_uppercase = "LIFE IN ISOLATION: BLACK FAMILIES LIVING IN A PREDOMINANTLY WHITE COMMUNITY"
title_all_uppercase = "PARTIAL-WAVE ANALYSIS OF ELASTIC-SCATTERING AND INELASTIC-SCATTERING OF DIRAC PARTICLES"
title_all_uppercase = "AN EXPLORATION OF PERSONALITY TRAITS IN DAUGHTERS OF LESBIAN MOTHERS (GENDER IDENTITY, SEXUAL ORIENTATION, ADJUSTMENT)"
title_all_uppercase = "SURVIVAL, MUTAGENESIS AND ONCOGENIC TRANSFORMATION OF CULTURED MAMMALIAN CELLS EXPOSED TO ULTRAVIOLET LIGHT"
title_all_uppercase = "THE STRUGGLE FOR STABILITY: AMERICAN POLICY TOWARD FRANCE, 1921-1933"




























print(f"Current title:{title_all_uppercase}=")

"""
	Use a character space as the delimiter between words/tokens in the title.

	If acronyms or a term needs to be all in upper case, or mxied case,
		fix the result/output manually.
"""

# Delmit tokens in the title with a character space.
tokenized_words = title_all_uppercase.split(" ")
# Placeholder for words/tokens that are properly capitalized.
capitalized_tokenized_words = ""
# Enumerate the list of words.
for x in tokenized_words:
	x = x.capitalize()
	capitalized_tokenized_words += " "
	capitalized_tokenized_words += x
	#capitalized_tokenized_words += " "
print(f"Fixed title:{capitalized_tokenized_words}=")

"""
	The result is:
	Metaheuristics: From Design To Implementation

	Corporate America Is At A Critical Crossroads
"""