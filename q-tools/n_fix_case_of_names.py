#!/usr/local/bin/python3

"""
	This is written by Zhiyang Ong to convert a list of names for the "Author" or "Editor" fields in BibTeX into the proper letter case.

	A number of publications, such as those from the National Academies Press, tend to list the names of authors in upper case (or capitals). Hence, we need to fix the letter case for these names before entering them into a reference management software or databases of references, such as BibTeX databases.




#### TO BE FIXED
	This script does not work for the following string of names.
+ JAMES J. DUDERSTADT and ERICH BLOCH and RAY M. BOWEN and BARRY HOROWITZ and LEE L. HUNTSMAN and JAMES H. {JOHNSON JR.} and KRISTINA M. JOHNSON and LINDA P. B. KATEHI and DAVID C. MOWERY and CHERRY A. MURRAY and MALCOLM R. {O'NEILL} and GEORGE SCALISE and ERNEST T. SMERDON and ROBERT F. SPROULL and DAVID N. WORMLEY
	- Problems:
		* {johnson Jr.}
			+ Problem with being enclosed in curly braces, and the failure to capitalize the first alphabetic letter/character.
		* {o'neill}
			+ Problem with being enclosed in curly braces, and the failure to capitalize letters around the second-letter apostrophe "'".
+ Norman R. Augustine and Craig Barrett and Gail Cassell and Nancy Grasmick and Charles {holliday Jr.} and Shirley Ann Jackson and Anita K. Jones and Richard Levin and C. D. (dan) {mote Jr.}
	- Problems:
		* {holliday Jr.}
			+ Problem with being enclosed in curly braces, and the failure to capitalize the first alphabetic letter/character.
		* (dan)
			+ Problem with being enclosed in round brakets, and the failure to capitalize the first alphabetic letter/character.
		* {mote Jr.}
			+ Problem with being enclosed in curly braces, and the failure to capitalize the first alphabetic letter/character.
+ Helen R. Quinn and Wyatt W. Anderson and Tanya Atwater and Philip Bell and Thomas B. Corcoran and Rodolfo Dirzo and Phillip A. Griffiths and Dudley R. Herschbach and Linda P. B. Katehi and John C. Mather and Brett D. Moulding and Jonathan Osborne and James W. Pellegrino and Stephen L. Pruitt and  and Brian Reiser and Rebecca R. {Richards-Kortum} and Walter G. Secada and Deborah C. Smith and Heidi A. Schweingruber and Thomas E. Keller and Michael A. Feder and Martin Storksdieck and Kelly A. Duncan and Rebecca Krone and Steven Marcus
	- Problems:
		* {richards-kortum}
			+ Problem with being enclosed in curly braces, and the failure to capitalize the first alphabetic letter/character and the first alphabetic letter/character after the hyphen.
+ THOMAS CONNELLY and PHILLIP SHARP and DENNIS AUSIELLO and MARIANNE {BRONNER-FRASER} and INGRID BURKE and JOHN BURRIS and JONATHAN EISEN and ANTHONY JANETOS and RICHARD KARP and PETER KIM and DOUGLAS LAUFFENBURGER and MARY LIDSTROM and WENDELL LIM and MARGARET {MCFALL-NGAI} and ELLIOT MEYEROWITZ and KEITH YAMAMOTO
	- {bronner-fraser}
	- {mcfall-ngai}
+ ALBERT CARNESALE and WILLIAM CHAMEIDES and DONALD F. BOESCH and MARILYN A. BROWN and JONATHAN CANNON and THOMAS DIETZ and GEORGE C. EADS and ROBERT W. FRI and JAMES E. GERINGER and DENNIS L. HARTMANN and CHARLES O. {HOLLIDAY, JR.} and KATHARINE L. JACOBS and THOMAS KARL and DIANA M. LIVERMAN and PAMELA A. MATSON and PETER H. RAVEN and RICHARD SCHMALENSEE and PHILIP R. SHARP and PEGGY M. SHEPARD and ROBERT H. SOCOLOW and SUSAN SOLOMON and BJORN STIGSON and THOMAS J. WILBANKS and PETER ZANDAN
	- {holliday, Jr.}
+ HAROLD T. SHAPIRO and MARK S. WRIGHTON and JOHN F. AHEARNE and ALLEN J. BARD and JAN BEYEA and WILLIAM F. BRINKMAN and DOUGLAS M. CHAPIN and STEVEN CHU and CHRISTINE A. {EHLIG-ECONOMIDES} and ROBERT W. FRI and CHARLES H. GOODMAN and JOHN B. HEYWOOD and LESTER B. LAVE and JAMES J. MARKOWSKY and RICHARD A. MESERVE and WARREN F. {MILLER, JR.} and FRANKLIN M. ('LYNN') {ORR, JR.} and LAWRENCE T. PAPAY and ARISTIDES A. N. PATRINOS and MICHAEL P. RAMAGE and MAXINE L. SAVITZ and ROBERT H. SOCOLOW and JAMES L. SWEENEY and G. DAVID TILMAN and C. MICHAEL WALTON
	- {ehlig-economides}
	- {miller, Jr.}
	- ('lynn')
	- {orr, Jr.}
+ THOMAS E. EVERHART and MARK L. GREEN and TANYA STYBLO BEDER and JAMES O. BERGER and LUIS A. CAFFARELLI and EMMANUEL J. CANDES and PHILLIP COLELLA and DAVID EISENBUD and PETER WILCOX JONES and JU-LEE KIM and YANN {LeCUN} and JUN LIU and JUAN MALDACENA and JOHN W. MORGAN and YUVAL PERES and EVA TARDOS and MARGARET H. WRIGHT and JOE B. WYATT
	- Ju-lee
	- {lecun}
+ ROBERT L. POPP and MICHAEL J. WILLIAMS and PETER A. BELING and JANIS A. {CANNON-BOWERS} and SCOTT T. GRAFTON and SUSAN HACKWOOD and STEPHAN KOLITZ and STEVEN KORNGUTH and FREDERICK R. LOPEZ and LAURA A. {McNAMARA} and CHRISTOPHER NEMETH and MICHAEL I. POSNER and ALAN R. WASHBURN and GEROLD YONAS and GREG L. ZACHARIAS
	- {cannon-bowers}
	- {mcnamara}
+ ANTOINETTE TAYLOR and ANTHONY {DeMARIA} and BRADLEY G. BOONE and STEVEN R. J. BRUECK and NANCY (NAOMI) HALAS and HENDRIK F. HAMANN and EVELYN HU and PETER {PALFFY-MUHORAY} and STANLEY ROGERS and JERRY A. SIMMONS and EDWIN THOMAS and ELI YABLONOVITCH
	- {demaria}
	- (naomi)
	- {palffy-muhoray}
+ MARTIN L PERL and CHARLES BALTAY and MARTIN BREIDENBACH and GERALD FEINBERG and HOWARD A. GORDON and LAWRENCE W. JONES and BOYCE D. {MCDANIEL} and FRANK S. MERRITT and ROBERT B. PALMER and JAMES M. PATERSON and JOHN {PEOPLES, JR.} and CHRIS QUIGG and DAVID M. RITSON and DAVID N. SCHRAMM and A. J. STEWART SMITH and MARK W. STROVINK and DONALD C. SHAPERO
	- {mcdaniel}
	- {peoples, Jr.}
+ ERIN K. {O'SHEA} and PETER G. WOLYNES and ROBERT H. AUSTIN and BONNIE L. BASSLER and CHARLES R. CANTOR and WILLIAM F. CARROLL and THOMAS R. CECH and CHRISTOPHER B. FIELD and GRAHAM R. FLEMING and ROBERT J. FULL and SHIRLEY ANN JACKSON and LAURA L. KIESSLING and CHARLES M. {LOVETT, JR.} and DIANNE NEWMAN and MONICA OLVERA {de la CRUZ} and JOS{\'{e}} N. ONUCHIC and GREGORY A. PETSKO and ASTRID PRINZ and CHARLES V. SHANK and BORIS I. SHRAIMAN and H. EUGENE STANLEY and GEORGE M. WHITESIDES
	- {o'shea}
	- {lovett, Jr.}
	- {de La Cruz}
	- Jos{'{e}}
+ R. BYRON PIPES and REZA ABBASCHIAN and ERIK ANTONSSON and THOMAS S. BABIN and BRUCE BOARDMAN and TIMOTHY J. CONSIDINE and JONATHAN DANTZIG and MARK GERSH and GEORGE T. (RUSTY) {GRAY III} and ELIZABETH A. HOLM and DAVID A. KOSHIBA and MORRIS H. {MORGAN III} and DANIEL E. WHITNEY
	- (rusty)
	- {gray Iii}
	- {morgan Iii}
+ SUSAN {DESMOND-HELLMANN} and CHARLES L. SAWYERS and DAVID R. COX and CLAIRE {FRASER-LIGGETT} and STEPHEN J. GALLI and DAVID B. GOLDSTEIN and DAVID J. HUNTER and ISAAC S. KOHANE and MANUEL LLIN{\'{A}}S and BERNARD LO and TOM MISTELI and SEAN J. MORRISON and DAVID G. NICHOLS and MAYNARD V. OLSON and CHARMAINE D. ROYAL and KEITH R. YAMAMOTO
	- {desmond-hellmann}
	- {fraser-liggett}
	- Llin{'{a}}s
+ MICHAEL T. CLEGG and CUTBERTO GARZA and JUDITH KIMBLE and C. D. (DAN) {MOTE JR.}
	- (dan)
	- {mote Jr.}























	References:

	Citations/references that use the LaTeX/BibTeX notation are taken from my BibTeX database
		(set of BibTeX entries).

	If these citations are not found in this list of references, information about them can be found in my BibTeX database.

	+ 


"""



#	A sample list of names from \cite{Jordan2013}.
names_all_uppercase = "MICHAEL I. JORDAN and KATHLEEN M. CARLEY and RONALD R. COIFMAN and DANIEL J. CRICHTON and MICHAEL J. FRANKLIN and ANNA C. GILBERT and ALEX G. GRAY and TREVOR J. HASTIE and PIOTR INDYK and THEODORE JOHNSON and DIANE LAMBERT and DAVID MADIGAN and MICHAEL W. MAHONEY and F. MILLER MALEY and CHRISTOPHER OLSTON and YORAM SINGER and ALEXANDER SANDOR SZALAY and TONG ZHANG"
names_all_uppercase = "ALEX LYKKEN and ANDY WHITE and JENNIFER SAM"
names_all_uppercase = "ASANKHA PALLEGEDARA"
names_all_uppercase = "RACHEL THOMAS and MARIANNE COOPER and GINA CARDAZONE and KATE URBAN and ALI BOHRER and MADISON LONG and LAREINA YEE and ALEXIS KRIVKOVICH and JESS HUANG and SARA PRINCE and ANKUR KUMAR and SARAH COURY"
names_all_uppercase = "LAWRENCE CHARLES PAULSON"
names_all_uppercase = "JAMES J. DUDERSTADT and ERICH BLOCH and RAY M. BOWEN and BARRY HOROWITZ and LEE L. HUNTSMAN and JAMES H. {JOHNSON JR.} and KRISTINA M. JOHNSON and LINDA P. B. KATEHI and DAVID C. MOWERY and CHERRY A. MURRAY and MALCOLM R. {O'NEILL} and GEORGE SCALISE and ERNEST T. SMERDON and ROBERT F. SPROULL and DAVID N. WORMLEY"
names_all_uppercase = "Freeman A. Hrabowski and James H. Ammons and Sandra {Begay-Campbell} and Beatriz Chu Clewell and Nancy S. Grasmick and Carlos G. Gutierrez and Evelynn M. Hammonds and Wesley L. Harris and Sylvia Hurtado and James S. Jackson and Shirley Mathis {McBay} and Diana Natalicio and John C. Nemeth and Eduardo J. Padr{\'{o}}n and Willie Pearson and Sidney A. Ribeau and John Brooks Slaughter and Richard Tapia and Lydia {Villa-Komaroff} and Linda Sue Warner"
names_all_uppercase = "NORMAN R. AUGUSTINE and CRAIG BARRETT and GAIL CASSELL and NANCY GRASMICK and CHARLES {HOLLIDAY JR.} and SHIRLEY ANN JACKSON and ANITA K. JONES and RICHARD LEVIN and C. D. (DAN) {MOTE JR.}"
names_all_uppercase = "HELEN R. QUINN and WYATT W. ANDERSON and TANYA ATWATER and PHILIP BELL and THOMAS B. CORCORAN and RODOLFO DIRZO and PHILLIP A. GRIFFITHS and DUDLEY R. HERSCHBACH and LINDA P. B. KATEHI and JOHN C. MATHER and BRETT D. MOULDING and JONATHAN OSBORNE and JAMES W. PELLEGRINO and STEPHEN L. PRUITT and  and BRIAN REISER and REBECCA R. {RICHARDS-KORTUM} and WALTER G. SECADA and DEBORAH C. SMITH and HEIDI A. SCHWEINGRUBER and THOMAS E. KELLER and MICHAEL A. FEDER and MARTIN STORKSDIECK and KELLY A. DUNCAN and REBECCA KRONE and STEVEN MARCUS"
names_all_uppercase = "THOMAS CONNELLY and PHILLIP SHARP and DENNIS AUSIELLO and MARIANNE {BRONNER-FRASER} and INGRID BURKE and JOHN BURRIS and JONATHAN EISEN and ANTHONY JANETOS and RICHARD KARP and PETER KIM and DOUGLAS LAUFFENBURGER and MARY LIDSTROM and WENDELL LIM and MARGARET {MCFALL-NGAI} and ELLIOT MEYEROWITZ and KEITH YAMAMOTO"
names_all_uppercase = "ALBERT CARNESALE and WILLIAM CHAMEIDES and DONALD F. BOESCH and MARILYN A. BROWN and JONATHAN CANNON and THOMAS DIETZ and GEORGE C. EADS and ROBERT W. FRI and JAMES E. GERINGER and DENNIS L. HARTMANN and CHARLES O. {HOLLIDAY, JR.} and KATHARINE L. JACOBS and THOMAS KARL and DIANA M. LIVERMAN and PAMELA A. MATSON and PETER H. RAVEN and RICHARD SCHMALENSEE and PHILIP R. SHARP and PEGGY M. SHEPARD and ROBERT H. SOCOLOW and SUSAN SOLOMON and BJORN STIGSON and THOMAS J. WILBANKS and PETER ZANDAN"
names_all_uppercase = "HAROLD T. SHAPIRO and MARK S. WRIGHTON and JOHN F. AHEARNE and ALLEN J. BARD and JAN BEYEA and WILLIAM F. BRINKMAN and DOUGLAS M. CHAPIN and STEVEN CHU and CHRISTINE A. {EHLIG-ECONOMIDES} and ROBERT W. FRI and CHARLES H. GOODMAN and JOHN B. HEYWOOD and LESTER B. LAVE and JAMES J. MARKOWSKY and RICHARD A. MESERVE and WARREN F. {MILLER, JR.} and FRANKLIN M. ('LYNN') {ORR, JR.} and LAWRENCE T. PAPAY and ARISTIDES A. N. PATRINOS and MICHAEL P. RAMAGE and MAXINE L. SAVITZ and ROBERT H. SOCOLOW and JAMES L. SWEENEY and G. DAVID TILMAN and C. MICHAEL WALTON"
names_all_uppercase = "MARVIN L. ADAMS and DAVID M. HIGDON and JAMES O. BERGER and DEREK BINGHAM and WEI CHEN and ROGER GHANEM and OMAR GHATTAS and JUAN MEZA and ERIC MICHIELSSEN and VIJAYAN N. NAIR and CHARLES W. NAKHLEH and DOUGLAS NYCHKA and STEPHEN M. POLLOCK and HOWARD A. STONE and ALYSON G. WILSON and MICHAEL R. ZIKA"
names_all_uppercase = "JOSEPH S. FRANCISCO and ROBERT G. BERGMAN and CHARLES T. KRESGE and DOUGLAS RAY"
names_all_uppercase = "BRUCE WINSTEIN and EUGENE BEIER and JAMES BRAU and PERSIS DRELL and GARY FELDMAN and JEROME FRIEDMAN and HOWARD GEORGI and DAVID J. GROSS and LAWRENCE J. HALL and STEPHEN HOLMES and EUGENE LOH and HUGH E. MONTGOMERY and NAN PHINNEY and THOMAS ROSER and MARJORIE SHAPIRO and MELVYN SHOCHET and FRANK WILCZEK and MICHAEL WITHERELL and MICHAEL E. ZELLER and DONALD C. SHAPERO and ROBERT L. RIEMER"
names_all_uppercase = "THOMAS E. EVERHART and MARK L. GREEN and TANYA STYBLO BEDER and JAMES O. BERGER and LUIS A. CAFFARELLI and EMMANUEL J. CANDES and PHILLIP COLELLA and DAVID EISENBUD and PETER WILCOX JONES and JU-LEE KIM and YANN {LeCUN} and JUN LIU and JUAN MALDACENA and JOHN W. MORGAN and YUVAL PERES and EVA TARDOS and MARGARET H. WRIGHT and JOE B. WYATT"
names_all_uppercase = "ROBERT L. POPP and MICHAEL J. WILLIAMS and PETER A. BELING and JANIS A. {CANNON-BOWERS} and SCOTT T. GRAFTON and SUSAN HACKWOOD and STEPHAN KOLITZ and STEVEN KORNGUTH and FREDERICK R. LOPEZ and LAURA A. {McNAMARA} and CHRISTOPHER NEMETH and MICHAEL I. POSNER and ALAN R. WASHBURN and GEROLD YONAS and GREG L. ZACHARIAS"
names_all_uppercase = "ANTOINETTE TAYLOR and ANTHONY {DeMARIA} and BRADLEY G. BOONE and STEVEN R. J. BRUECK and NANCY (NAOMI) HALAS and HENDRIK F. HAMANN and EVELYN HU and PETER {PALFFY-MUHORAY} and STANLEY ROGERS and JERRY A. SIMMONS and EDWIN THOMAS and ELI YABLONOVITCH"
names_all_uppercase = "ROBERT J. HERMANN and WILLIAM BAESLACK and EDWARD C. DOWLING and THOMAS W. EAGAR and JOSEPH A. HEIM and KARL KEMPF and MAX LAGALLY and JAMES MATTICE and ANTHONY C. MULLIGAN and JACK SOLOMON and JOEL YUDKEN"
names_all_uppercase = "MARTIN L PERL and CHARLES BALTAY and MARTIN BREIDENBACH and GERALD FEINBERG and HOWARD A. GORDON and LAWRENCE W. JONES and BOYCE D. {MCDANIEL} and FRANK S. MERRITT and ROBERT B. PALMER and JAMES M. PATERSON and JOHN {PEOPLES, JR.} and CHRIS QUIGG and DAVID M. RITSON and DAVID N. SCHRAMM and A. J. STEWART SMITH and MARK W. STROVINK and DONALD C. SHAPERO"
names_all_uppercase = "ERIN K. {O'SHEA} and PETER G. WOLYNES and ROBERT H. AUSTIN and BONNIE L. BASSLER and CHARLES R. CANTOR and WILLIAM F. CARROLL and THOMAS R. CECH and CHRISTOPHER B. FIELD and GRAHAM R. FLEMING and ROBERT J. FULL and SHIRLEY ANN JACKSON and LAURA L. KIESSLING and CHARLES M. {LOVETT, JR.} and DIANNE NEWMAN and MONICA OLVERA {de la CRUZ} and JOS{\'{e}} N. ONUCHIC and GREGORY A. PETSKO and ASTRID PRINZ and CHARLES V. SHANK and BORIS I. SHRAIMAN and H. EUGENE STANLEY and GEORGE M. WHITESIDES"
names_all_uppercase = "R. BYRON PIPES and REZA ABBASCHIAN and ERIK ANTONSSON and THOMAS S. BABIN and BRUCE BOARDMAN and TIMOTHY J. CONSIDINE and JONATHAN DANTZIG and MARK GERSH and GEORGE T. (RUSTY) {GRAY III} and ELIZABETH A. HOLM and DAVID A. KOSHIBA and MORRIS H. {MORGAN III} and DANIEL E. WHITNEY"
names_all_uppercase = "HAROLD T. SHAPIRO and SALLY DAWSON and NORMAN R. AUGUSTINE and JONATHAN A. BAGGER and PHILIP N. BURROWS and SANDRA M. FABER and STUART J. FREEDMAN and JEROME I. FRIEDMAN and DAVID J. GROSS and JOSEPH S. HEZIR and NORBERT HOLTKAMP and TAKAAKI KAJITA and NEAL F. LANE and NIGEL LOCKYER and SIDNEY R. NAGEL and HOMER A. NEAL and J. RITCHIE PATTERSON and HELEN QUINN and CHARLES V. SHANK and PAUL STEINHARDT and HAROLD E. VARMUS and EDWARD WITTEN"
names_all_uppercase = "SUSAN {DESMOND-HELLMANN} and CHARLES L. SAWYERS and DAVID R. COX and CLAIRE {FRASER-LIGGETT} and STEPHEN J. GALLI and DAVID B. GOLDSTEIN and DAVID J. HUNTER and ISAAC S. KOHANE and MANUEL LLIN{\'{A}}S and BERNARD LO and TOM MISTELI and SEAN J. MORRISON and DAVID G. NICHOLS and MAYNARD V. OLSON and CHARMAINE D. ROYAL and KEITH R. YAMAMOTO"
# This script works for characters with accents (or, diacritics or diacritical marks).
names_all_uppercase = "LLINÁS"

names_all_uppercase = "MICHAEL T. CLEGG and CUTBERTO GARZA and JUDITH KIMBLE and C. D. (DAN) {MOTE JR.}"
names_all_uppercase = "ROBERT PAUL KURSHAN"
names_all_uppercase = "C. D. (DAN) {MOTE, JR.} and JOHN GANNON and RAKESH AGRAWAL and ROBERT BRODERSEN and DANIEL T. CHIU and JACQUELINE FLETCHER and PAUL C. GAILEY and HENDRIK F. HAMANN and DANIEL E. HASTINGS and THOMAS R. HOWELL and DONALD H. LEVY and FRANCES S. LIGLER and HEATHER J. {MacLEAN} and FAWWAZ T. ULABY and KATHLEEN A. WALSH and HEATHER WILSON"
names_all_uppercase = "YOSHIHIRO FRANCIS FUKUYAMA"
names_all_uppercase = "JOSEPH ALLEN FISHER"
names_all_uppercase = "ROBERT LEROY MERCER"
names_all_uppercase = "JULIE ANN SCHWARTZ"
names_all_uppercase = "GERALD LOKCHUNG CHAN"
names_all_uppercase = "MELVYN PAUL LEFFLER"
names_all_uppercase = "RUAIRI ARRIETA-KENNA AND AMY GUNIA"
names_all_uppercase = "ELOISE BARRY"
















print(f"Current list of names:{names_all_uppercase}=")

"""
	Use a character space as the delimiter between entities in the list of names.

	Names of different co-authors are separated by " and ".

	Names of each (co-)author, such as their first/given name, family/surname, or middle name, are separated by a character space.

	There are (co-)authors with compound surnames, such as double/double-barrelled/hyphenated/triple-barrelled surnames, or some other compound surname (such as those that contain nobiliary particles to reflect the nobility of their family or family name affixes).

	There are (co-)authors with compound given names.

	Also, there are (co-)authors that have their names written only in lower case.

	The names are statistically not going to be in all lower case.
	For a significant number of times, they appear in all upper case.

	Skip checking if the list of names is all in upper case before proceeding.

	This is because I use " and " to connect full names together, and to distinguish a full name, or personal name, from another.
	Hence, the list of names would never be all in upper case.
	If I use " AND " instead, my solution would capitalize it to an upper case
		first character/letter, and I need to make it lower case later.



	+ For the "and" separator between the names of multiple co-authors, leave the case as it is.

	+ For tokens that have multiple alphabetical characters, keep the first letter of that token in upper case and the rest in lower case.

	+ For tokens that have only one alphabetical character, keep this character in upper case.
"""

# Delmit tokens in the list of names with a character space.
tokenized_names = names_all_uppercase.split(" ")
# Placeholder for names/tokens that are properly capitalized.
capitalized_tokenized_names = ""
# Enumerate the list of tokens obtained from the list of names.
for x in tokenized_names:
	# Is the currently enumerated token not referring to "and"?
	if "and" != x:
		"""
			Yes. Make the first letter of the token upper case,
				and the rest of the token's characters lower case.
		"""
		x = x.capitalize()
		#capitalized_tokenized_names += x.capitalize()
	# Else, do nothing.
	capitalized_tokenized_names += " "
	capitalized_tokenized_names += x
	#capitalized_tokenized_names += " "
print("-----------------------------------")
print(f"Fixed list of names:{capitalized_tokenized_names}=")

"""
	The result is:
	Michael I. Jordan and Kathleen M. Carley and Ronald R. Coifman and Daniel J. Crichton and Michael J. Franklin and Anna C. Gilbert and Alex G. Gray and Trevor J. Hastie and Piotr Indyk and Theodore Johnson and Diane Lambert and David Madigan and Michael W. Mahoney and F. Miller Maley and Christopher Olston and Yoram Singer and Alexander Sandor Szalay and Tong Zhang

	Alex Lykken and Andy White and Jennifer Sam

	Rachel Thomas and Marianne Cooper and Gina Cardazone and Kate Urban and Ali Bohrer and Madison Long and Lareina Yee and Alexis Krivkovich and Jess Huang and Sara Prince and Ankur Kumar and Sarah Coury
"""
