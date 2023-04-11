#!/usr/local/bin/python3

"""
	This is written by Zhiyang Ong to convert a list of names for the "Author" or "Editor" fields in BibTeX into the following format.

	[given name or its initial] [optional middle name(s) or initials of middle names] [family name (or surname)].

	Some software, such as a BibDesk, or a version thereof, and some publishers/publications list their names in the following format.

	[family name (or surname)], [given name or its initial] [optional middle name(s) or initials of middle names]

	Hence, to improve readability, we need to rearrange the format of names into the initial format for these names before entering them into a reference management software or databases of references, such as BibTeX databases.






	#### TO BE FIXED
	This script does not work for the following string of names.
	+ "{\"
		- The backslash character, if not the open curly brace, disappears, since it and the subsequent character are not valid escape characters in Python.
		- This bug is demonstrated in processing the following string of names.
		- "Kohlas, J{\"{u}}rg and Meyer, Bertrand and Schiper, Andr{\'{e}}"
		- "Kozyrakis, Christoforos E. and Perissakis, Stylianos and Patterson, David and Anderson, Thomas and Asanovi{\'{c}}, Krste and Cardwell, Neal and Fromm, Richard and Golbus, Jason and Gribstad, Benjamin and Keeton, Kimberly and Thomas, Randi and Treuhaft, Noah and Yelick, Katherine"
		- "L{\"{u}}dtke, Niklas and Panzeri, Stefano and Brown, Martin and Broomhead, David S. and Knowles, Joshua and Montemurro, Marcelo A. and Kell, Douglas B."
		- "Ma, Zhe and Marchal, Pol and Scarpazza, Daniele Paolo and Yang, Peng and Wong, Chun and G{\'{o}}mez, Jos{\'{e}} Ignacio and Himpe, Stefaan and {Ykman-Couvreur}, Chantal and Catthoor, Francky"
		- "Berndtsson, Mikael and Hansson, J{\"{o}}rgen and Olsson, Bj{\"{o}}rn and Lundell, Bj{\"{o}}rn"
		- Atasu, Kubilay and Mencer, Oskar and Luk, Wayne and {\"{O}}zturan, Can and D{\"{u}}ndar, Gunhan
		- Adve, Sarita and Albonesi, David H. and Brooks, David and Ceze, Luis and Dwarkadas, Sandhya and Emer, Joel and Falsafi, Babak and Gonzalez, Antonio and Hill, Mark D. and Irwin, Mary Jane and Kaeli, David and Keckler, Stephen W. and Kozyrakis, Christos and Lebeck, Alvin and Martin, Milo and Mart{\'\i}nez, Jos{\'{e}} F. and Martonosi, Margaret and Olukotun, Kunle and Oskin, Mark and Peh, Li-Shiuan and Prvulovic, Milos and Reinhardt, Steven K. and Schulte, Michael and Sethumadhavan, Simha and Sohi, Guri and Sorin, Daniel and Torrellas, Josep and Wenisch, Thomas F. and Wood, David and Yelick, Katherine
		- {Mangione-Smith}, William H. and Hutchings, Brad and Andrews, David and DeHon, Andr{\'{e}} and Ebeling, Carl and Hartenstein, Reiner and Mencer, Oskar and Morris, John and Palem, Krishna and Prasanna, Viktor K. and Spaanenburg, Henk A. E.
		- Nagpal, Radhika and Zambonelli, Franco and Sirer, Emin G{\"{u}}n and Chaouchi, Hakima and Smirnov, Mikhail
		- Narayanan, Rajeev and Akbarpour, Behzad and Zaki, Mohamed H. and Tahar, Sofi{\`{e}}ne and Paulson, Lawrence C.
		- Bofill, Miquel and Palah{\'{i}}, Miquel and Suy, Josep and Villaret, Mateu
		- Bruttomesso, Roberto and Cimatti, Alessandro and Franz{\'{e}}n, Anders and Griggio, Alberto and Hanna, Ziyad and Nadel, Alexander and Palti, Amit and Sebastiani, Roberto
		- Barroso, Luiz Andr{\'{e}} and Clidaras, Jimmy and H{\={o}}lzle, Urs
			* Also, has "\=".
		- Kowalik, Miko{\l}aj and Gothard, Chris M. and Drews, Aaron M. and Gothard, Nosheen A. and Weckiewicz, Alex and Fuller, Patrick E. and Grzybowski, Bartosz A. and Bishop, Kyle J. M.
		- Dyo, Vladimir and Ellwood, Stephen A. and Macdonald, David W. and Markham, Andrew and Mascolo, Cecilia and P{\'{a}}sztor, Bence and Scellato, Salvatore and Trigoni, Niki and Wohlers, Ricklef and Yousef, Kharsim
		- Fr{\"{a}}nzle, Martin and Herde, Cristian and Teige, Tino and Ratschan, Stefan and Schubert, Tobias
		- Gajski, Daniel D. and Zhu, Jianwen and D{\"{o}}mer, Rainer and Gerstlauer, Andreas and Zhao, Shuqing
		- Frevert, Ronny and Haase, Joachim and Jancke, Roland and Kn{\"{o}}chel, Uwe and Schwarz, Peter and Kakerow, Ralf and Darianian, Mohsen
		- Babar, Muhammad Ali and Dings{\o}yr, Torgeir and Patricia Lago, Hans {van Vliet}
		- Dubois, Michel and Annavaram, Murali and Stenstr{\"{o}}m, Per
		- Sokolsky, Oleg and Lee, Insup and Ben-Abdallah, Han{\^{e}}ne
		- Clough, G. Wayne and Agogino, Alice M. and {Campbell, Jr.}, George and Chavez, James and Craig, David O. and {Cruz, Jr.}, Jos{\'{e}} B. and Girshman, Peggy and Hastings, Daniel E. and Heller, Michael J. and Johnson, Deborah G. and Kay, Alan C. and Khalil, Tarek M. and Lucky, Robert W. and Mulvey, John M. and Nunes, Sharon L. and Petroski, Henry and Rosser, Sue V. and Smerdon, Ernest T.
		- {McCallum}, William G. and {Hughes-Hallett}, Deborah and Gleason, Andrew M. and Kalayci{\^{o}}glu, Selin and Lahme, Brigitte and Lock, Patti Frazer and Lozano, Guadalupe I. and Morris, Jerry and Mumford, David and Osgood, Brad G. and Patterson, Cody L. and Quinney, Douglas and Spiegler, Adam H. and {Tecosky-Feldman}, Jeff and Tucker, Thomas W.
		- {Hughes-Hallett}, Deborah and Gleason, Andrew M. and {McCallum}, William G. and Connally, Eric and Flath, Daniel E. and Kalayci{\^{0}}glu, Selin and Brigitte Lahme, Patti Frazer Lock, David O. Lomen David Lovelock Guadalupe I. Lozano Jerry Morris David Mumford Brad G. Osgood Cody L. Patterson Douglas Quinney Karen Rhea Adam H. Spiegler Jeff Tecosky-Feldman Thomas W. Tucker
		- Dr{\'{e}}o, Johann and Siarry, Patrick and P{\'{e}}trowski, Alain and Taillard, Eric
		- Cave, Vincent and Cledat, Romain and Tasirlar, Sagnak and Chatterjee, Sanjay and Budimlic, Zoran and Knauerhase, Rob and Carter, Nicholas P.
			* Cav{\'{e}}, Vincent
			* Cledat, Romain
			* Ta{c{s}}{\i}rlar, Sa{u{g}}nak
				+ modified to avoid SyntaxError
					- SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 5615-5616: truncated [uXXXX] escape
					- Python scripts cannot handle backslash C and backslash U in the source code.
					- The accents or diacritics involving the backslash C and backslash U are removed, even in the comments. "backslash U" is the main problem.
			* Chatterjee, Sanjay
			* Budimli{\'{c}}, Zoran
			* Knauerhase, Rob
			* Carter, Nicholas P.
		- Eisley, Noel and Peh, {Li-Shiuan} and Shang, Li
		- Agarwal, Niket and Peh, {Li-Shiuan} and Jha, Niraj K.
		- Seo, Daeho and Ali, Akif and Lim, {Won-Taek} and Rafique, Nauman and Thottethodi, Mithuna
		- Torquati, Massimo and Bertels, Koen and Karlsson, Sven and Pacull, Fran{\c{c}}ois
		- Cota, {\'{E}}rika and {de Morais Amory}, Alexandre and Lubaszewski, Marcelo Soares
		- Gebali, Fayez and Elmiligi, Haytham and {El-Kharashi}, Mohamed Watheq
		- Monchiero, Matteo and Canal, Ramon and Gonz{\'{a}}lez, Antonio
		- Jaleel, Aamer and Hasenplaugh, William and Qureshi, Moinuddin and Sebot, Julien and {Steely Jr.}, Simon and Emer, Joel
		- Colwell, Robert P. and Nix, Robert P. and {O'Donnell}, John J. and Papworth, David B. and Rodman, Paul K.
		- Budimli{\'{c}}, Zoran and Sarkar, Vivek and Cav{\'{e}}, Vincent and Chatterjee, Sanjay and Majeti, Deepak
		- Barab{\'{a}}si, Albert-L{\'{a}}szl{\'{o}} and Bly, Adam and Boch, Wolfgang and Gharajedaghi, Jamshid and Gosselin, Derrick P. and Guterl, Fred and Helbing, Dirk and Heylighen, Francis and Kitano, Hiroaki and Smith, Christopher H. Llewellyn and {Al Mansoori}, Ahmed Obaid and {Mitleton-Kelly}, Evangelia and Sanders, T. Irene and Saraph, Anupam and Vasbinder, Jan Wouter and West, Geoffrey B. and Wouters, Alain
		- Sarkar, Vivek and Burke, Michael and Budimli{\'{c}}, Zoran and Charles, Philippe and Shirako, Jun and Zhao, Jisheng and Kumar, Vivek and Cav{\'{e}}, Vincent and Hayashi, Akihiro and Bhandari, Kumud and Grossman, Max and Imam, Shams and Majeti, Deepak and Sb{\^{i}}rlea, Drago{{s}} Dumitru and Sb{\^{i}}rlea, Alina Gabriela and Sharma, Kamal and Surendran, Rishi and Ta{{s}}{\i}rlar, Sa{{g}}nak and Vrvilo, Nick and Zhang, Yunming and Kurihara, Kyle and Xue, Bing and Baraniuk, Rich and Cartwright, Corky and Chaudhuri, Swarat and Cooper, Keith and {Mellor-Crummey}, John and Simar, Ray and Jermaine, Chris and Torczon, Linda and Zhong, Lin and Aggarwal, Sanjeev and Bronevetsky, Greg and Bui, Alex and Cledat, Romain and Cong, Jason and Dennis, Jack and Gao, Guang and Grove, David and Knauerhase, Rob and Knobe, Kathleen and McGraw, Jim and Nandivada, Krishna and Newton, Ryan and Quinlan, Dan and Palsberg, Jens and Peshansky, Igor and Reinman, Glenn and Yelick, Kathy and Agarwal, Ashutosh and Breen, Emma and Cumber, Keisha and Diehl, Stephanie and Du, Odette and Gupta, Amit and Keshan, Adarsh and Lee, Hubert and Lee, Jungwoo (Eric) and Micheloni, Lauren and Payne, Jarred and Spare, Caleb and Zhao, Matthew and Zou, Xiangjin (Rho) and Barik, Rajkishore and Chatterjee, Sanjay and Guo, Yi and Joyner, Mack and Raman, Raghavan and Barik, Rajkishore and Shirako, Jun and Westbrook, Edwin and Yan, Yonghong and Zhao, Jisheng and Koelbel, Charles
			* Diacritics or accents for the following are removed, since the
				Python interpreter complains about them via the following error:
				- Latin circumflex, which chevron-shaped is allowed.
				- The accents or diacritics involving the backslash C and backslash U are removed.
				- The error is the SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 7781-7782: truncated [uXXXX] escape
					* modified to avoid SyntaxError
					* Reminder: Python scripts cannot handle backslash C and backslash U in the source code, even in the comments. "backslash U" is the main problem.
		- Hamano, Junio C. and Torvalds, Linus and Pearce, Shawn and Schindelin, Johannes and Pitre, Nicolas and Scharfe, Ren{\'{e}} and King, Jeff and Nieder, Jonathan and Herland, Johan and Sixt, Johannes and Rabbelier, Sverre and Gruber, Michael J. and Duy, Nguy{\~{e}}n Th{\'{a}}i Ng{\d{o}}c and Bjarmason, {\AE}var Arnfj{\"{o}}r{\dh} and Rast, Thomas
		- {van de Vijver}, Marc J. and He, Yudong D. and {van 't Veer}, Laura J. and Dai, Hongyue and Hart, Augustinus A. M. and Voskuil, Dorien W. and Schreiber, George J. and Peterse, Johannes L. and Roberts, Chris and Marton, Matthew J. and Parrish, Mark and Atsma, Douwe and Witteveen, Anke and Glas, Annuska and Delahaye, Leonie and {van der Velde}, Tony and Bartelink, Harry and Rodenhuis, Sjoerd and Rutgers, Emiel T. and Friend, Stephen H. and and Ren{\'{e}} Bernards
		- Barnasconi, Martin and Grimm, Christoph and Damm, Markus and Einwich, Karsten and Lou{\"{e}}rat, Marie-Minerve and Maehne, Torsten and Pecheux, Fran{\c{c}}ois and Vachoux, Alain
		- Guimer{\`{a}}, Roger and Sales-Pardo, Marta and Amaral, Lu{\'{i}}s A. N.
		- Breuer, Melvin and Chakradhar, Srimat and Joyner, William and Kumar, Rakesh and Raghunathan, Anand and Shanbhag, Naresh and Kurdahi, Fadi and Henkel, J{\"o}rg and Yeh, David
		- Fern{\'{a}}ndez, Francisco V. and Rodr{\'{i}}guez-V{\'{a}}zquez, Angel and Huertas, Jos{\'{e}} L. and Gielen, Georges G. E.
		- Fedder, Gary K. and Howe, Roger T. and Liu, Tsu-Jae King and Qu{\'{e}}vy, Emmanuel P.
		- Brualdi, Richard A. and Cvetkovi{\'{c}}, Drago{backslash u{s}}
			* "{ backslash u" causes problems during run time. Comment it out. And, do it manually.
		- Ausl{\"{a}}nder, Simon and Ausl{\"{a}}nder, David and M{\"{u}}ller, Marius and Wieland, Markus and Fussenegger, Martin
		- Balint, Adrian and Belov, Anton and Diepold, Daniel and Gerber, Simon and J{\"{a}}rvisalo, Matti and Sinz, Carsten
		- Ismail, Mohammed and Franca, Jos{\'{e}}
		- Drechsler, Rolf and Eggersgl{\"{u}}{\ss}, Stephan and Fey, G{\"{o}}rschwin and Tille, Daniel
		- Darte, Alain and Robert, Yves and Vivien, Fr{\'{e}}d{\'{e}}ric
	+ "$\b"
		- This is because Python treats the backslash as an escape character, and '\b' translates to the backslash character.
		- This results in deleting the previous character, a '$' (dollar sign).
		- This bug is demonstrated in processing the following string of names.
		- "Wille, Robert and Gro{$\beta$}e, Daniel and Haedicke, Finn and Drechsler, Rolf"
 	+ When a mixed-case name (first name, last name, or a middle name) or a double-barrelled name (or hyphenated surname) is wrapped in curly braces, the captialization of the name is incorrect.
 		- If the first alphabetical letter of the name is not the first character of the first, middle, or last name, it would not be characterized correctly.
 		- The first letter of the appending name in a double-barrelled name would not be capitalized either.
	+ "{\r"
		- {\r{A}}str{\"{o}}m, Karl Johan and Murray, Richard M.
	+ "{\v"
		- 
		- Caponetto, Riccardo and Dongola, Giovanni and Fortuna, Luigi and Petr{\'{a}}{\v{s}}, Ivo
		- Alur, R. and Dang, T. and Esposito, J. and Fierro, R. and Hur, Y. and Ivan{\v{c}}i{\'{c}}, F. and Kumar, V. and Lee, I. and Mishra, P. and Pappas, G. and Sokolsky, O.
		- Chatterjee, Shouri and Pun, {Kong Pang} and Stani{\'{c}}, Neboj{\v{s}}a and Tsividis, Yannis and Kinget, Peter
		- {\v{C}}iegis, Raimondas and Henty, David and K{\r{a}}gstr{\"{o}}m, Bo and {\v{Z}}ilinskas, Julius
		- G{\"{a}}rtner, Bernd and Matou{\v{s}}ek, Ji{\v{r}}{\'{i}}











	References:

	Citations/references that use the LaTeX/BibTeX notation are taken from my BibTeX database
		(set of BibTeX entries).

	If these citations are not found in this list of references, information about them can be found in my BibTeX database.

	+ 


"""



#	A sample list of names from \cite{Keiter2013a}.
names_last_first__middle_format = "Keiter, Eric R. and Russo, Thomas V. and Schiek, Richard L. and Sholander, Peter E. and Thornquist, Heidi K. and Mei, Ting and Verley, Jason C. and Baur, David G."

names_last_first__middle_format = "Kellerer, Hans and Pferschy, Ulrich and Pisinger, David"
names_last_first__middle_format = "Kempf, Torsten and Ascheid, Gerd and Leupers, Rainer"
names_last_first__middle_format = "Kerbyson, Darren J. and Vishnu, Abhinav and Barker, Kevin J. and Hoisie, Adolfy"
names_last_first__middle_format = "Kevenaar, T. A. M. and {ter Maten}, E. J. W. and Janssen, H. H. J. M. and Onneweer, S. P."
names_last_first__middle_format = "Khatri, Sunil P. and Brayton, Robert K. and {Sangiovanni-Vincentelli}, Alberto L."
names_last_first__middle_format = "Khoshgoftaar, Taghi M. and Allen, Edward B. and Halstead, Robert and Trio, Gary P. and Flass, Ronald M."
names_last_first__middle_format = "Khursheed, Saqib and Al-Hashimi, Bashir M. and Chakrabarty, Krishnendu and Harrod, Peter"
names_last_first__middle_format = "Khursheed, Saqib and Al-Hashimi, Bashir M. and Harrod, Peter"
names_last_first__middle_format = "Kifer, Michael and Smolka, Scott A."
names_last_first__middle_format = "Kim, Hyesoon and Vuduc, Richard and Baghsorkhi, Sara and Choi, Jee and Hwu, {Wen-mei}"
names_last_first__middle_format = "Kim, Jintae and Lee, Jaeseo and Vandenberghe, Lieven and Yang, {Chih-Kong} Ken"
names_last_first__middle_format = "Ebbinghaus, {H.-D.} and Flum, J. and Thomas, W."
names_last_first__middle_format = "Knickerbocker, J. U. and Andry, P. S. and Dang, B. and Horton, R. R. and Patel, C. S. and Polastre, R. J. and Sakuma, K. and Sprogis, E. S. and Tsang, C. K. and Webb, B. C. and Wright, S. L."
names_last_first__middle_format = "Knickerbocker, J. U. and Andry, P. S. and Dang, B. and Horton, R. R. and Interrante, M. J. and Patel, C. S. and Polastre, R. J. and Sakuma, K. and Sirdeshmukh, R. and Sprogis, E. J. and Sri-Jayantha, S. M. and Stephens, A. M. and Topol, A. W. and Tsang, C. K. and Webb, B. C. and Wright, S. L."
names_last_first__middle_format = "Koelbl, Alfred and Jacoby, Reily and Jain, Himanshu and Pixley, Carl"
names_last_first__middle_format = "Koeppl, Heinz and Setti, Gianluca and {di Bernardo}, Mario and Densmore, Douglas"
names_last_first__middle_format = "Kogel, Tim and Leupers, Rainer and Meyr, Heinrich"
names_last_first__middle_format = "Kohlas, J{\"{u}}rg and Meyer, Bertrand and Schiper, Andr{\'{e}}"
names_last_first__middle_format = "Korte, Bernhard and Rautenbach, Dieter and Vygen, Jens"
names_last_first__middle_format = "Kortuem, Gerd and Fitton, Daniel and Kawsar, Fahim and Sundramoorth, Vasughi"
names_last_first__middle_format = "Kozyrakis, Christoforos E. and Perissakis, Stylianos and Patterson, David and Anderson, Thomas and Asanovi{\'{c}}, Krste and Cardwell, Neal and Fromm, Richard and Golbus, Jason and Gribstad, Benjamin and Keeton, Kimberly and Thomas, Randi and Treuhaft, Noah and Yelick, Katherine"
names_last_first__middle_format = "Krebs, Christopher P. and Lindquist, Christine H. and Warner, Tara D. and Fisher, Bonnie S. and Martin, Sandra L."
names_last_first__middle_format = "Krishnaswamy, Smita and Ren, Haoxing and Modi, Nilesh and Puri, Ruchir"
names_last_first__middle_format = "Krogh, Bruce H. and Lee, Edward and Lee, Insup and Mok, Al and Pappas, George and Rajkumar, Raj and Sha, Lui Raymond and {Sangiovanni-Vincentelli}, Alberto and Shin, Kang and Stankovic, Jack and Sztipanovits, Janos and Wolf, Wayne and Zhao, Wei"
names_last_first__middle_format = "Krogh, Bruce H. and Lee, Edward and Lee, Insup and Mok, Al and Pappas, George and Rajkumar, Raj and Rubin, Harvey and {Sangiovanni-Vincentelli}, Alberto and Sha, Lui and Shin, Kang and Stankovic, Jack and Sztipanovits, Janos and Wolf, Wayne and Zhao, Wei"
names_last_first__middle_format = "Kumar, Akash and Corporaal, Henk and Mesman, Bart and Ha, Yajun"
names_last_first__middle_format = "Kundert, Ken and Chang, Henry and Jefferies, Dan and Lamant, Gilles and Malavasi, Enrico and Sendig, Fred"
names_last_first__middle_format = "Kundu, Sudipta and Lerner, Sorin and Gupta, Rajesh K."
names_last_first__middle_format = "Kuo, Chin-Cheng and Chen, Yen-Lung and Tsai, I-Ching and Chan, Li-Yu and Liu, Chien-Nan Jimmy"
names_last_first__middle_format = "Kurdila, Andrew J. and Pardalos, Panos M. and Zabarankin, Michael"
names_last_first__middle_format = "Kurumahmut, B. and Kabukcu, G. and Ghamari, R. and Yurdakul, A."
names_last_first__middle_format = "Lai, Yung-Te and Pedram, Massoud and Vrudhula, Sarma B. K."
names_last_first__middle_format = "Bertozzi, Carolyn and Ahearne, John F. and Ayala, Francisco J. and Bertozzi, Andrea L. and Bishop, David J. and Comstock, Gary L. and Houle, Frances A. and Johnson, Deborah G. and Loui, Michael C. and {Richard-Kortum}, Rebecca R. and Steneck, Nicholas H. and Zigmond, Michael J."
names_last_first__middle_format = "Toga, Arthur W. and Rosen, Bruce and Wedeen, Van J."
names_last_first__middle_format = "Hu, Chenming and Niknejad, Ali M. and Chauhan, Yogesh Singh and Khandelwal, Sourabh and Sachid, Angada and Duarte, Juan Pablo"
names_last_first__middle_format = "Hu, Chenming and Ko, Ping and Cao, Mark and Chan, Mansun and Xi, Xuemei (Jane) and Chen, James C. and Chen, Kai and Cheng, Yuhua and Dunga, Mohan and Huang, JianHui and Hui, Kelvin and Jeng, MinChie and Jin, Xiaodong and Liu, Weidong and Liu, ZhiHong and Tu, Robert"
names_last_first__middle_format = "Grune, Dick and {van Reeuwijk}, Kees and Bal, Henri E. and Jacobs, Ceriel J.H. and Langendoen, Koen"
names_last_first__middle_format = "Lee, Hyunseok and Lin, Yuan and Harel, Yoav and Woh, Mark and Mahlke, Scott and Mudge, Trevor and Flautner, Krisztian"
names_last_first__middle_format = "Merolla, Paul and Arthur, John and Akopyan, Filipp and Imam, Nabil and Manohar, Rajit and Modha, Dharmendra S."
names_last_first__middle_format = "Lewyn, Lanny L. and Ytterdal, Trond and Wulff, Carsten and Martin, Kenneth"
names_last_first__middle_format = "Lexau, Jon and Zheng, Xuezhe and Bergey, Jon and Krishnamoorthy, Ashok V. and Ho, Ron and Drost, Robert and Cunningham, Jack"
names_last_first__middle_format = "Bonham, Ann and Cohen, Jordan and Florez, Jose and Gibbons, Gary and Jenkins, Renee and Jordan, Tuajuanda and Riley, Wayne J. and Ruffin, John and Silverstein, Samuel C. and Tabak, Lawrence A. and Takagi, Dana Yasu and Tuckson, Reed and Velez, Maria Teresa and Wilson, M. Roy and Yamamoto, Keith R. and Yancy, Clyde"
names_last_first__middle_format = "Hamacher, Carl and Vranesic, Zvonko and Zaky, Safwat and Manjikian, Naraig"
names_last_first__middle_format = "Lin, Weisi and Tao, Dacheng and Kacprzyk, Janusz and Li, Zhu and Izquierdo, Ebroul and Wang, Haohong"
names_last_first__middle_format = "Lindholm, Erik and Nickolls, John and Oberman, Stuart and Montrym, John"
names_last_first__middle_format = "Anderson, James A. and Pellionisz, Andras and Rosenfeld, Edward"
names_last_first__middle_format = "Hunt, Brian R. and Lipsman, Ronald L. and Rosenberg, Jonathan M. and Coombes, Kevin R. and Osborn, John E. and Stuck, Garrett J."
names_last_first__middle_format = "Hunt, Brian R. and Lipsman, Ronald L. and Rosenberg, Jonathan M. and Coombes, Kevin R. and Osborn, John E. and Stuck, Garrett J."
names_last_first__middle_format = "Nicholls, John G. and Martin, A. Robert and Fuchs, Paul A. and Brown, David A. and Diamond, Mathew E. and Weisblat, David A."
names_last_first__middle_format = "Little, Scott and Walter, David and Myers, Chris and Thacker, Robert and Batchu, Satish and Yoneda, Tomohiro"
names_last_first__middle_format = "L{\"{u}}dtke, Niklas and Panzeri, Stefano and Brown, Martin and Broomhead, David S. and Knowles, Joshua and Montemurro, Marcelo A. and Kell, Douglas B."
names_last_first__middle_format = "Lux, Matthew W. and Bramlett, Brian W. and Ball, David A. and Peccoud, Jean"
names_last_first__middle_format = "Ma, Zhe and Marchal, Pol and Scarpazza, Daniele Paolo and Yang, Peng and Wong, Chun and G{\'{o}}mez, Jos{\'{e}} Ignacio and Himpe, Stefaan and {Ykman-Couvreur}, Chantal and Catthoor, Francky"
names_last_first__middle_format = "Zopounidis, Constantin and Doumpos, Michael and Pardalos, Panos M."
names_last_first__middle_format = "Berndtsson, Mikael and Hansson, J{\"{o}}rgen and Olsson, Bj{\"{o}}rn and Lundell, Bj{\"{o}}rn"
names_last_first__middle_format = "Chartrand, Gary and Polimeni, Albert D. and Zhang, Ping"
names_last_first__middle_format = "Zikopoulos, Paul C. and Eaton, Chris and {deRoos}, Dirk and Deutsch, Thomas and Lapis, George"
names_last_first__middle_format = "Zheng, Ming and Barrera, Leah O. and Ren, Bing and Wu, Ying Nian"
names_last_first__middle_format = "Zhan, Yong and Kumar, Sanjay V. and Sapatnekar, Sachin S."
names_last_first__middle_format = "Yanushkevich, S. N. and Kasai, S. and Tangim, G. and Tran, A. H. and Mohamed, T. and Smerko, V. P."
names_last_first__middle_format = "Yan, Lu and Zhang, Yan and Yang, Laurence T. and Ning, Huansheng"
names_last_first__middle_format = "Xu, Yang and Hsiung, Kan-Lin and Li, Xin and Pileggi, Lawrence T. and Boyd, Stephen P."
names_last_first__middle_format = "Xidonas, Panos and Mavrotas, George and Krintas, Theodore and Psarras, John and Zopounidis, Constantin"
names_last_first__middle_format = "Xie, Jierui and Sreenivasan, Sameet and Korniss, Gyorgy and Zhang, Weituo and Lim, Chjan and Szymanski, Boleslaw K."
names_last_first__middle_format = "Xie, Zhen and Wroblewska, Liliana and Prochazka, Laura and Weiss, Ron and Benenson, Yaakov"
names_last_first__middle_format = "Wu, Xindong and Kumar, Vipin and Quinlan, J. Ross and Ghosh, Joydeep and Yang, Qiang and Motoda, Hiroshi and McLachlan, Geoffrey J. and Ng, Angus and Liu, Bing and Yu, Philip S. and Zhou, Zhi-Hua and Steinbach, Michael and Hand, David J. and Steinberg, Dan"
names_last_first__middle_format = "Wu, {Chi-An} and Lin, {Ting-Hao} and Lee, {Chih-Chun} and Huang, {Chung-Yang} (Ric)"
names_last_first__middle_format = "Woollard, David and Mattmann, Chris A. and Medvidovic, Nenad and Gil, Yolanda"
names_last_first__middle_format = "Woh, Mark and Seo, Sangwon and Lee, Hyunseok and Lin, Yuan and Mahlke, Scott and Mudge, Trevor and Chakrabarti, Chaitali and Flautner, Krisztian"
names_last_first__middle_format = "Steer, Michael B. and Christoffersen, Carlos and Kriplani, Nikhil and Luniya, Sonali and Lowry, Justin and Hart, Frank P. and Harris, Theodore Robert and Saunders, Chris and Priyadarshi, Shivam and Kanj, Houssam and Vijaychand, Shubha and Mohan, Ramya and Batty, Bill and Velu, Senthil and Bollapragada, Rajesh"

"""
	#### TO BE FIXED
	This script does not work for the following string of names.

	This is because Python treats the backslash as an escape character, and '\b' translates to the backslash character.
	+ This results in deleting the previous character, a '{' (open curly braces).
"""
names_last_first__middle_format = "Wille, Robert and Gro{$\beta$}e, Daniel and Haedicke, Finn and Drechsler, Rolf"

names_last_first__middle_format = "Wilimzig, Claudia and Ragert, Patrick and Dinse, Hubert R."
names_last_first__middle_format = "Weng, Yi-Peng and Chen, Hung-Ming and Chen, Tung-Chieh and Pan, Po-Cheng and Chen, Chien-Hung and Chen, Wei-Zen"
names_last_first__middle_format = "Warnock, J. D. and Keaty, J. M. and Petrovick, J. and Clabes, J. G. and Kircher, C. J. and Krauter, B. L. and Restle, P. J. and Zoric, B. A. and Anderson, C. J."
names_last_first__middle_format = "Wang, L. and Olbrich, M. and Barke, E. and B{\"{u}}chner, T. and B{\"{u}}hler, M. and Panitz, P."
names_last_first__middle_format = "Wang, Chao and Hachtel, Gary D. and Somenzi, Fabio"
names_last_first__middle_format = "Wang, Ying-Chih and Komuravelli, Anvesh and Zuliani, Paolo and Clarke, Edmund M."
names_last_first__middle_format = "Wang, Kang L. and Galatsis, Kosmas and Ostroumov, Roman and Khitun, Alexander and Zhao, Zuoming and Han, Song"
names_last_first__middle_format = "Wang, Alice and Calhoun, Benton H. and Chandrakasan, Anantha P."
names_last_first__middle_format = "Wane, Sidina and Kuo, An-Yu and Santos, Patrick Dos"
names_last_first__middle_format = "Walter, David and Little, Scott and Myers, Chris and Seegmiller, Nicholas and Yoneda, Tomohiro"
names_last_first__middle_format = "Walpole, Ronald E. and Myers, Raymond H. and Myers, Sharon L. and Ye, Keying"
names_last_first__middle_format = "Walker, George E. and Golde, Chris M. and Jones, Laura and Bueschel, Andrea Conklin and Hutchings, Pat"
names_last_first__middle_format = "Qiu, Robert C. and Chen, Zhe and Guo, Nan and Song, Yu and Zhang, Peng and Li, Husheng and Lai, Lifeng"
names_last_first__middle_format = "Atasu, Kubilay and Mencer, Oskar and Luk, Wayne and {\"{O}}zturan, Can and D{\"{u}}ndar, Gunhan"
names_last_first__middle_format = "Ooi, Melanie Po-Leen and Chan, Chris and Tee, Wey Jean and Kuang, Ye Chow and Kleeman, Lindsay and Demidenko, Serge"
names_last_first__middle_format = "Owens, John D. and Dally, William J. and Ho, Ron and Jayasimha, D. N. (Jay) and Keckler, Stephen W. and Peh, Li-Shiuan"
names_last_first__middle_format = "Oskin, Mark and Torrellas, Josep and Das, Chita and Davis, John and Dwarkadas, Sandhya and Eeckhout, Lieven and Feiereisen, Bill and Jimenez, Daniel and Hill, Mark and Kim, Martha and Larus, James and Martonosi, Margaret and Mutlu, Onur and Olukotun, Kunle and Putnam, Andrew and Sherwood, Tim and Smith, James and Wood, David and Zilles, Craig"
names_last_first__middle_format = "Agrawal, Divyakant and Bernstein, Philip and Bertino, Elisa and Davidson, Susan and Dayal, Umeshwar and Franklin, Michael and Gehrke, Johannes and Haas, Laura and Halevy, Alon and Han, Jiawei and Jagadish, H. V. and Labrinidis, Alexandros and Madden, Sam and Papakonstantinou, Yannis and Patel, Jignesh M. and Ramakrishnan, Raghu and Ross, Kenneth and Shahabi, Cyrus and Suciu, Dan and Vaithyanathan, Shiv and Widom, Jennifer"
names_last_first__middle_format = "Adve, Sarita and Albonesi, David H. and Brooks, David and Ceze, Luis and Dwarkadas, Sandhya and Emer, Joel and Falsafi, Babak and Gonzalez, Antonio and Hill, Mark D. and Irwin, Mary Jane and Kaeli, David and Keckler, Stephen W. and Kozyrakis, Christos and Lebeck, Alvin and Martin, Milo and Mart{\'\i}nez, Jos{\'{e}} F. and Martonosi, Margaret and Olukotun, Kunle and Oskin, Mark and Peh, Li-Shiuan and Prvulovic, Milos and Reinhardt, Steven K. and Schulte, Michael and Sethumadhavan, Simha and Sohi, Guri and Sorin, Daniel and Torrellas, Josep and Wenisch, Thomas F. and Wood, David and Yelick, Katherine"
names_last_first__middle_format = "Torrellas, Josep and Oskin, Mark and Adve, Sarita and Almasi, George and Ceze, Luis and Chtchelkanova, Almadena and Das, Chita and Feiereisen, Bill and Harrod, William and Hill, Mark and Hiller, Jon and Kannan, Sampath and Kant, Krishna and Kozyrakis, Christos and Larus, James and Murphy, Richard and Mutlu, Onur and Narayanasamy, Satish and Olukotun, Kunle and Patt, Yale and Sivasubramaniam, Anand and Skadron, Kevin and Strauss, Karin and Swanson, Steven and Tullsen, Dean"
names_last_first__middle_format = "{van Dam}, Andy and Foley, Jim and Guttag, John and Hanrahan, Pat and Johnson, Chris and Katz, Randy and Kelly, Henry and Lee, Peter and Shaw, David"
names_last_first__middle_format = "Duranton, Marc and Yehia, Sami and {De Sutter}, Bjorn and {De Bosschere}, Koen and Cohen, Albert and Falsafi, Babak and Gaydadjiev, Georgi and Katevenis, Manolis and Maebe, Jonas and Munk, Harm and Navarro, Nacho and Ramirez, Alex and Temam, Olivier and Valero, Mateo"
names_last_first__middle_format = "Goodwin, Graham C. and Graebe, Stefan F. and Salgado, Mario E."
names_last_first__middle_format = "Malewicz, Grzegorz and Austern, Matthew H. and Bik, Aart J. C. and Dehnert, James C. and Horn, Ilan and Leiser, Naty and Czajkowski, Grzegorz"
names_last_first__middle_format = "Mamidi, Suman and Blem, Emily R. and Schulte, Michael J. and Glossner, John and Iancu, Daniel and Iancu, Andrei and Moudgill, Mayan and Jinturkar, Sanjay"
names_last_first__middle_format = "{Mangione-Smith}, William H. and Hutchings, Brad and Andrews, David and DeHon, Andr{\'{e}} and Ebeling, Carl and Hartenstein, Reiner and Mencer, Oskar and Morris, John and Palem, Krishna and Prasanna, Viktor K. and Spaanenburg, Henk A. E."
names_last_first__middle_format = "Adve, Sarita V. and Burger, Doug and Eigenmann, Rudolf and Rawsthorne, Alasdair and Smith, Michael D. and Gebotys, Catherine H. and Kandemir, Mahmut T. and Lilja, David J. and Choudbary, Alok N. and Fang, Jesse Z. and Yew, {Pen-Chung}"
names_last_first__middle_format = "Manyika, James and Lund, Susan and Auguste, Byron and Mendonca, Lenny and Welsh, Tim and Ramaswamy, Sreenivas"
names_last_first__middle_format = "Brayton, Robert K. and Hachtel, Gary D. and McMullen, Curtis T. and {Sangiovanni-Vincentelli}, Alberto L."
names_last_first__middle_format = "Long, Fred and Mohindra, Dhruv and Seacord, Robert C. and Sutherland, Dean F. and Svoboda, David"
names_last_first__middle_format = "Manyika, James and Chui, Michael and Brown, Brad and Bughin, Jacques and Dobbs, Richard and Roxburgh, Charles and Byers, Angela Hung"
names_last_first__middle_format = "Manyika, James and Chui, Michael and Bughin, Jacques and Dobbs, Richard and Bisson, Peter and Marrs, Alex"
names_last_first__middle_format = "Manyika, James and Sinclair, Jeff and Dobbs, Richard and Strube, Gernot and Rassey, Louis and Mischke, Jan and Remes, Jaana and Roxburgh, Charles and George, Katy and O'Halloran, David and Ramaswamy, Sreenivas"
names_last_first__middle_format = "Mason, Jonathan and Linsay, Paul S. and Collins, J. J. and Glass, Leon"
names_last_first__middle_format = "Mathew, J. and Rahaman, H. and Singh, A. K. and Jabir, A. M. and Pradhan, D. K."
names_last_first__middle_format = "Mathew, J. and Jabir, A. M. and Singh, A. K. and Rahaman, H. and Pradhan, D. K."
names_last_first__middle_format = "Theodoridis, Sergios and Pikrakis, Aggelos and Koutroumbas, Konstantinos and Cavouras, Dionisis"
names_last_first__middle_format = "Melikyan, V. Sh. and Movsisyan, V. M. and Bozoyan, Sh. E. and Simonyan, S. H. and Vardanyan, R. R. and Maranjyan, H. B. and Buniatyan, V. V. and Khudaverdyan, S. Kh. and Petrosyan, S. G. and Babayan, A. H. and Harutyunyan, A. G. and Travajyan, M. G. and Gomtsyan, H. A. and Muradyan, M. A. and Yeghiazaryan, V. S. and Ayvazyan, G. E. and Vardanyan, V. A. and Melkonyan, S. V. and Minasyan, A. K. and Tumanyan, A. K. and Hahanov, V. I. and Umnyashkin, S. V. and Petkovich, P. M. and Al-Hashash, H. and Gritschneder, D. M. and Stepanyan, H. L. and Tananyan, H. G. and Ghazaryan, E. M. and Krupkina, T. Yu. and Majzoub, S. and Albasha, L. and Assi, A. and Aloul, F. and Hayrapetyan, D. B."
names_last_first__middle_format = "Melikyan, Vazgen and Markosyan, Gayane and Asatryan, Anna and Minasyan, Tamar and Babayan, Eduard"
names_last_first__middle_format = "Menzies, Tim and Port, Dan and Chen, Zhihao and Hihn, Jairus"
names_last_first__middle_format = "Metodi, Tzvetan S. and Faruque, Arvin I. and Chong, Frederic T."
names_last_first__middle_format = "Rao, Vasant B. and Overhauser, David V. and Trick, Timothy N. and Hajj, Ibrahim N."
names_last_first__middle_format = "Coulter, Chris and Maughan, Alistair and Delaney, John F. and Hanson, Vivian L. and Ford, Christopher D. and Knox, Thomas J. and Stevenson, Scott W. and Jahn, Paul E. and Schwartz, William I. and Weiss, Russell G. and Beraha, Stuart S. and Meister, Gabriel E. and Milner, Gordon"
names_last_first__middle_format = "Myers, Chris and Barker, Nathan and Kuwahara, Hiroyuki and Madsen, Curtis and Nguyen, Nam and Winstead, Chris"
names_last_first__middle_format = "Nastov, Ognen and Telichevesky, Rircardo and Kundert, Ken and White, Jacob"
names_last_first__middle_format = "Casier, Herman and Steyaert, Michiel and {van Roermund}, Arthur H. M."
names_last_first__middle_format = "Cimatti, Alessandro and Griggio, Alberto and Schaafsma, Bastiaan Joost and Sebastiani, Roberto"
names_last_first__middle_format = "Conte, Thomas M. and Dubey, Pradeep K. and Jennings, Matthew D. and Lee, Ruby B. and Peleg, Alex and Rathnam, Salliah and Schlansker, Mike and Song, Peter and Wolfe, Andrew"
names_last_first__middle_format = "Nowatzki, Tony and Ferris, Michael and Sankaralingam, Karthikeyan and Estan, Cristian and Vaish, Nilay and Wood, David"
names_last_first__middle_format = "Nuzzo, Pierluigi and Sun, Xuening and Wu, Chang-Ching and {De Bernardinis}, Fernando and {Sangiovanni-Vincentelli}, Alberto"
names_last_first__middle_format = "Felt, Eric and Malavasi, Enrico and Charbon, Edoardo and Totaro, Roberto and {Sangiovanni-Vincentelli}, Alberto"
names_last_first__middle_format = "Pal{\'{a}}ncz, B{\'{e}}la and Beny{\'{o}}, Zolt{\'{a}}n and Kov{\'{a}}cs, Levente"
names_last_first__middle_format = "Palkovic, Martin and Raghavan, Praveen and Li, Min and Dejonghe, Antoine and {Van der Perre}, Liesbet and Catthoor, Francky"
names_last_first__middle_format = "Gothard, Chris M. and Soh, Siowling and Gothard, Nosheen A. and Kowalczyk, Bartlomiej and Wei, Yanhu and Baytekin, Bilge and Grzybowski, Bartosz A."
names_last_first__middle_format = "Parab, Jivan S. and Shelake, Vinod G. and Kamat, Rajanish K. and Naik, Gourish M."
names_last_first__middle_format = "Fowler, Martin and Beck, Kent and Brant, John and Opdyke, William and Roberts, Don"
names_last_first__middle_format = "Patt, Yale N. and Patel, Sanjay J. and Evers, Marius and Friendly, Daniel H. and Stark, Jared"
names_last_first__middle_format = "Pryputniewicz, Ryszard J. and Przekwas, Andrzej J. and Turowski, Marek and Furmanczyk, Michal and Hieke, Andreas and Pryputniewicz, Dariusz R."
names_last_first__middle_format = "Sankaralingam, Karthikeyan and Nagarajan, Ramadass and McDonald, Robert and Desikan, Rajagopalan and Drolia, Saurabh and Govindan, M. S. and Gratz, Paul and Gulati, Divya and Hanson, Heather and Kim, Changkyu and Liu, Haiming and Ranganathan, Nitya and Sethumadhavan, Simha and Sharif, Sadia and Shivakumar, Premkishore and Keckler, Stephen W. and Burger, Doug"
names_last_first__middle_format = "Luu, Jason and Goeders, Jeffrey and Wainberg, Michael and Somerville, Andrew and Yu, Thien and Nasartschuk, Konstantin and Nasr, Miad and Wang, Sen and Liu, Tim and Ahmed, Nooruddin and Kent, Kenneth B. and Anderson, Jason and Rose, Jonathan and Betz, Vaughn"
names_last_first__middle_format = "Betz, Vaughn and Rose, Jonathan and Luu, Jason and Anderson, Jason and Kent, Kenneth and Somerville, Andrew and Jamieson, Peter and Goeders, Jeffrey and Rubin, Rafi and Yu, Chiwai and Jarvin, Mark and Grant, David and Goel, Manish and Kwong, Joyce and Rudolph, Jeff and Milankov, Peter and Wang, Cong and Densmore, Opal and {O'Brian}, Patty and Campbell, Ted and Fang, {Wek-Mark} and Marquardt, Alexander and Furrow, Ash"
names_last_first__middle_format = "Ronse, K. and Jansen, Ph. and Gronheid, R. and Hendrickx, E. and Maenhoudt, M. and Goethals, M. and Vandenberghe, G."
names_last_first__middle_format = "Rosen, Kenneth H. and Michaels, John G. and Gross, Jonathan L. and Grossman, Jerrold W. and Shier, Douglas R."
names_last_first__middle_format = "Rosen, Kenneth H. and Host, Douglas A. and Klee, Rachel and Farber, James and Rosinski, Richard"
names_last_first__middle_format = "Benjamin, Ben Varkey and Gao, Peiran and McQuinn, Emmett and Choudhary, Swadesh and Chandrasekaran, Anand R. and Bussat, {Jean-Marie} and {Alvarez-Icaza}, Rodrigo and Arthur, John V. and Merolla, Paul A. and Boahen, Kwabena"
names_last_first__middle_format = "Boccardi, Federico and {Heath ,Jr.}, Robert W. and Lozano, Angel and Marzetta, Thomas L. and Popovski, Petar"
names_last_first__middle_format = "Keiter, Eric R. and Russo, Thomas V. and Schiek, Richard and Thornquist, Heidi and Mei, Ting and Verley, Jason and Baur, David and Sholander, Pete and Hutchinson, Scott"
names_last_first__middle_format = "Vigder, Mark and Vinson, Norman G. and Singer, Janice and Stewart, Darlene and Mews, Keith"
names_last_first__middle_format = "Gachovska, Tanya K. and Hudgins, Jerry L. and Santi, Enrico and Bryant, Angus and Palmer, Patrick R."
names_last_first__middle_format = "Gachovska, Tanya Kirilova and Du, Bin and Hudgins, Jerry L. and Santi, Enrico"
names_last_first__middle_format = "Aggarwal, Ankur O. and Raj, P. Markondeya and Abothu, Isaac R. and Sacks, Michael D. and Tay, Andrew A. O. and Tummala, Rao R."
names_last_first__middle_format = "Tummala, Rao R. and Swaminathan, Madhavan and Tentzeris, Manos M. and Laskar, Joy and Chang, Gee-Kung and Sitaraman, Suresh and Keezer, David and Senior Member, IEEE, Daniel Guidotti Zhaoran Huang Kyutae Lim Lixi Wan Swapan K. Bhattacharya Venkatesh Sundaram Fuhan Liu and Raj, P. Markondeya"
names_last_first__middle_format = "Tummala, Rao R. and Sundaram, Venky and Chatterjee, Ritwik and Raj, P. Markondeya and Kumbhat, Nitesh and Sukumaran, Vijay and Sridharan, Vivek and Choudury, Abhishek and Chen, Qiao and Bandyopadhyay, Tapobrata"
names_last_first__middle_format = "Bagheri, Rahim and Mirzaei, Ahmad and Chehrazi, Saeed and Heidari, Mohammad E. and Lee, Minjae and Mikhemar, Mohyee and Tang, Wai K. and Abidi, Asad A."
names_last_first__middle_format = "Tselentis, Georgios and Domingue, John and Galis, Alex and Gavras, Anastasius and Hausheer, David and Krco, Srdjan and Lotz, Volkmar and Zahariadis, Theodore"
names_last_first__middle_format = "Dongarra, Jack and Foster, Ian and Fox, Geoffrey and Gropp, William and Kennedy, Ken and Torczon, Linda and White, Andy"
names_last_first__middle_format = "Topol, Anna W. and {La Tulipe, Jr.}, Douglas C. and Shi, Leathen and Frank, David J. and Bernstein, Kerry and Steen, Steven E. and Kumar, Arvind and Singco, Gilbert U. and Young, Albert M. and Guarini, Kathryn W. and Leong, Meikei"
names_last_first__middle_format = "Track, Elie K. and Conte, Tom and Allwood, Dan and Atienza, David and Candelaria, Jonathan and {DeBenedictis}, Erik and Gargini, Paolo and Gulak, Glen and Hoang, Bichlien and Iyer, Subramanian (Subu) and Lu, {Yung-Hsiang} and Holmes, Scott and Kadin, Alan M. and Mountain, David and Mukhanov, Oleg and Oklobdzijja, Vojin G. and Stavrou, Angelos and Tonti, Bill and Young, Ian"
names_last_first__middle_format = "Grundmann, Susan Tsui and Wagner, Anne M. and Rose, Mary M. and Crum, John and Shugrue, Laura and Roth, Sharon"
names_last_first__middle_format = "Tanaka, Mikiko Sode and Takeuchi, Osamu and Ogawa, Hayato and Ono, Mituhiro and Uchida, Hiroaki and Sasaki, Hideki"
names_last_first__middle_format = "Lyons, Damian M. and {Papadakis-Kanaris}, Christina and Weiss, Gary M. and Werschulz, Arthur G."
names_last_first__middle_format = "Stan, Mircea R. and Franzon, Paul D. and Goldstein, Seth Copen and Lach, John C. and Ziegler, Matthew M."
names_last_first__middle_format = "Spinellis, Diomidis and Vidalis, Michael J. and O'Kelly, Michael E. J. and Papadopoulos, Chrissoleon T."
names_last_first__middle_format = "Basili, Victor R. and Cruzes, Daniela and Carver, Jeffrey C. and Hochstein, Lorin M. and Hollingsworth, Jeffrey K. and Zelkowitz, Marvin V. and Shull, Forrest"
names_last_first__middle_format = "Gaster, Benedict R. and Howes, Lee and Kaeli, David R. and Mistry, Perhaad and Schaa, Dana"
names_last_first__middle_format = "Emer, Joel and Hill, Mark D. and Patt, Yale N. and Yi, Joshua J. and Chiou, Derek and Sendag, Resit"
names_last_first__middle_format = "Blaauw, David and Dutta, Prabal and Fu, Kevin and Guestrin, Carlos and Jafari, Roozbeh and Jones, Doug and Kubiatowicz, John and Kumar, Vijay and Lee, Edward A. and Murray, Richard and Pappas, George and Rabaey, Jan and Rowe, Anthony and {Sangiovanni-Vincentelli}, Alberto and Sechen, Carl M and Seshia, Sanjit A. and Rosing, Tajana Simunic and Taskar, Ben and Wawrzynek, John and Wessel, David"
names_last_first__middle_format = "Haensch, Wilfried and Nowak, Edward J. and Dennard, Robert H. and Solomon, P. M. and Bryant, Andres and Dokumaci, Omer H. and Kumar, Arvind and Wang, Xinlin and Johnson, Jeffrey B. and Fischetti, Massimo V."
names_last_first__middle_format = "Bourdopoulos, George I and Pnevmatikakis, Aristodemos and Anastassopoulos, Vassilis and Deliyannis, Theodore L"
names_last_first__middle_format = "Shung, C. S. and Jain, R. and Rimey, K. and Wang, E. and Srivastava, M. B. and Lettang, E. and Azim, S. K. and Hilfinger, P. N. and Rabaey, J. and Brodersen, R. W."
names_last_first__middle_format = "Albrecht, Vera and Barker, Phil and Borley, Steven J. and Brorson, Stuart and Dezai, Glao S. and Flax, Matt and Foci, Daniele and Gillespie, Alan and Inbody, Chris and Jones, Stefan and Lemaitre, Laurent and Nenzi, Paolo and Peters, Arno W. and Popescu, Serban-Mihai and Post, Georg and Rouat, Emmanuel and Cluque, Lionel Sainte and Tanaka, Hitoshi and Tiel, Stephan and Vogt, Holger and Warning, Dietmar and Widlok, Michael and Williams, Charles D.H."
names_last_first__middle_format = "Shanbhag, Naresh R. and Mitra, Subhasish and {de Veciana}, Gustavo and Orshansky, Michael and Marculescu, Radu and Roychowdhury, Jaijeet and Jones, Douglas and Rabaey, Jan M."
names_last_first__middle_format = "Adam, Laura and Kozar, Michael and Letort, Gaelle and Mirat, Olivier and Srivastava, Arunima and Stewart, Tyler and Wilson, Mandy L and Peccoud, Jean"
names_last_first__middle_format = "Sahai, Anant and Tandra, Rahul and Mishra, Shridhar Mubaraq and Hoven, Niels"
names_last_first__middle_format = "Saiedian, Hossein and Bowen, Jonathan P. and Butler, Ricky W. and Dill, David L. and Glass, Robert L. and Gries, David and Hall, Anthony and Hinchey, Michael G. and Holloway, C. Michael and Jackson, Daniel and Jones, Cliff B. and Lutz, Michael J. and Parnas, David Lorge and Rushby, John and Wing, Jeannette and Zave, Pamela"
names_last_first__middle_format = "Salapura, Valentina and Bickford, Randy and Blumrich, Matthias and Bright, Arthur A. and Chen, Dong and Coteus, Paul and Gara, Alan and Giampapa, Mark and Gschwind, Michael and Gupta, Manish and Hall, Shawn and Haring, Ruud A. and Heidelberger, Philip and Hoenicke, Dirk and Kopcsay, Gerard V. and Ohmacht, Martin and Rand, Rick A. and Takken, Todd and Vranas, Pavlos"
names_last_first__middle_format = "Saleh, Resve and Wilton, Steve and Mirabbasi, Shahriar and Hu, Alan and Greenstreet, Mark and Lemieux, Guy and Pande, Partha Pratim and Grecu, Cristian and Ivanov, Andre"
names_last_first__middle_format = "McConaghy, Trent and Palmers, Pieter and Gao, Peng and Steyaert, Michiel and Gielen, Georges"
names_last_first__middle_format = "Dr{\'{e}}o, Johann and Siarry, Patrick and P{\'{e}}trowski, Alain and Taillard, Eric"
names_last_first__middle_format = "Cormen, Thomas H. and Leiserson, Charles E. and Rivest, Ronald L. and Stein, Clifford"
names_last_first__middle_format = "Wong, Ban and Zach, Franz and Moroz, Victor and Mittal, Anurag and Starr, Greg and Kahng, Andrew"
names_last_first__middle_format = "Keating, Michael and Flynn, David and Aitken, Robert and Gibbons, Alan and Shi, Kaijian"
names_last_first__middle_format = "Kent, Jim and Barber, Galt and Casper, Jonathan and Clawson, Hiram and Diekhans, Mark and Fujita, Pauline and Guruvadoo, Luvina and Harte, Rachel and Heitner, Steve and Hinrichs, Angie and Karolchik, Donna and Kuhn, Robert and Learned, Katrina and Lee, Brian and Pringle, Thomas and Raney, Brian and Rosenbloom, Kate and Speir, Matthew and Zweig, Ann"
names_last_first__middle_format = "Kent, Jim and Barber, Galt and Casper, Jonathan and Clawson, Hiram and Diekhans, Mark and Fujita, Pauline and Guruvadoo, Luvina and Harte, Rachel and Heitner, Steve and Hinrichs, Angie and Karolchik, Donna and Kuhn, Robert and Learned, Katrina and Lee, Brian and Pringle, Thomas and Raney, Brian and Rosenbloom, Kate and Speir, Matthew and Zweig, Ann"
names_last_first__middle_format = "Martin, Milo M. K. and Sorin, Daniel J. and Ailamaki, Anastassia and Alameldeen, Alaa R. and Dickson, Ross M. and Mauer, Carl J. and Moore, Kevin E. and Plakal, Manoj and Hill, Mark D. and Wood, David A."
names_last_first__middle_format = "Smith, J{\"{o}}hn Gro{$\beta$}e"
names_last_first__middle_format = "Bilir, E. Ender and Dickson, Ross M. and Hu, Ying and Plakal, Manoj and Sorin, Daniel J. and Hill, Mark D. and Wood, David A."
names_last_first__middle_format = "Batchelor, Colin and Corbett, Peter and Day, Aileen and Karapetyan, Kenneth and Pshenichnov, Alexey and Richardson, Susan and Sharpe, David and Steele, Jon and Tkachenko, Valery and Williams, Antony"
names_last_first__middle_format = "Bergman, Keren and Carloni, Luca P. and Biberman, Aleksandr and Chan, Johnnie and Hendry, Gilbert"
names_last_first__middle_format = "Binkert, Nathan and Beckmann, Bradford and Black, Gabriel and Reinhardt, Steven K. and Saidi, Ali and Basu, Arkaprava and Hestness, Joel and Hower, Derek R. and Krishna, Tushar and Sardashti, Somayeh and Sen, Rathijit and Sewell, Korey and Shoaib, Muhammad and Vaish, Nilay and Hill, Mark D. and Wood, David A."
names_last_first__middle_format = "Olukotun, Kunle and Nayfeh, Basem A. and Hammond, Lance and Wilson, Ken and Chang, Kunyung"
names_last_first__middle_format = "Hrishikesh, M. S. and Burger, Doug and Jouppi, Norman P. and Keckler, Stephen W. and Farkas, Keith I. and Shivakumar, Premkishore"
names_last_first__middle_format = "Coulon, Didier and Rospide, Sebastien and Penn, Malcolm and Bryant, Mike and Bosson, Laurent and Dubois, Guy"
names_last_first__middle_format = "Griffiths, Phillip A. and Alberts, Bruce M. and Brinkman, William F. and Challoner, David R. and Cowling, Ellis B. and Dinneen, Gerald P. and Flax, Alexander H. and Gomory, Ralph E. and Greenwood, M. R. C. and Hearn, Ruby P. and Koshland, Marian and Larson, Thomas D. and Liebowitz, Harold and {McFadden}, Daniel L. and Osborn, Mary J. and Shine, Kenneth I. and Tanenbaum, Morris and Wilson, William Julius and {McCray}, Lawrence E."
names_last_first__middle_format = "Benhamou, Eric and Katz, Randy H. and Barley, Stephen R. and Hargadon, Andrew B. and Kenney, Martin and Klepper, Steven and Lazowska, Edward D. and Mendonca, Lenny and Nagel, David C. and Prabhakar, Arati and Reddy, Raj and Sanders, Lucinda"
names_last_first__middle_format = "Kent, W. James and Sugnet, Charles W. and Furey, Terrence S. and Roskin, Krishna M. and Pringle, Tom H. and Zahler, Alan M. and Haussler, David"
names_last_first__middle_format = "{Ben-Ari}, Moti and Clancy, Mike and Cooper, Steve and Crescenzi, Pierluigi and Edwards, Steve and Grissom, Scott and Hundhausen, Chris and Karavirta, Ville and Korhonen, Ari and Kraemer, Eileen and Kucera, Ludek and Malmi, Lauri and McNally, Myles and Naps, Tom and Narayana, Hari and Rodger, Susan and Roessling, Guido and Ross, Rocky and Shaffer, Cliff and Stern, Linda"
names_last_first__middle_format = "Ono, Yukinori and Inokawa, Hiroshi and Takahashi, Yasuo and Nishiguchi, Katsuhiko and Fujiwara, Akira"
names_last_first__middle_format = "Bitton, Dina and DeWitt, David J. and Hsaio, David K. and Menon, Jaishankar"
names_last_first__middle_format = "Hagmann, Patric and Cammoun, Leila and Gigandet, Xavier and Meuli, Reto and Honey, Christopher J. and Wedeen, Van J. and Sporns, Olaf"
names_last_first__middle_format = "Dijk, Koene R. A. Van and Hedden, Trey and Venkataraman, Archana and Evans, Karleyton C. and Lazar, Sara W. and Buckner, Randy L."
names_last_first__middle_format = "Berger, Daniel and Burns, Randal and Bock, Davi and Cardona, Albert and Chung, Kwanghun and Chuang, Ming and Cook, Steven and Deisseroth, Karl and Emmons, Scott and Gray, Will and Grosenick, Logan and Hager, Greg and Kasthuri, Bobby and Kashdan, Misha and Kleissas, Dean and Lee, {Wei-Chung} Allen and Lichtman, Jeff and Lillaney, Kunal and Manavalan, Priya and Naiman, Kan and Padmanaban, Raghav and Perlman, Eric and Priebe, Carey and Reid, Clay and Saalfeld, Stefan and Sinha, Ayushi and Smith, Stephen and Szalay, Alexander and Vogelstein, Joshua T. and Weiler, Nick and Zheng, Da"
names_last_first__middle_format = "Barke, Erich and Grabowski, Darius and Graeb, Helmut and Hedrich, Lars and Heinen, Stefan and Popp, Ralf and Steinhorst, Sebastian and Wang, Yifan"
names_last_first__middle_format = "Lalgudi, S. N. and Srinivasan, K. and Casinovi, G. and Mandrekar, R. and Engin, E. and Swaminathan, M. and Kretchmer, Y."
names_last_first__middle_format = "Clark, J. V. and Zhou, N. and Bindel, D. and Schenato, L. and Wu, W. and Demmel, J. and Pister, K. S. J."
names_last_first__middle_format = "Clements, Paul and Bachmann, Felix and Bass, Len and Garlan, David and Ivers, James and Little, Reed and Merson, Paulo and Nord, Robert and Stafford, Judith"
names_last_first__middle_format = "Booch, Grady and Maksimchuk, Robert A. and Engle, Michael W. and Young, Bobbi J. and Conallen, Jim and Houston, Kelli A."
names_last_first__middle_format = "Buschmann, Frank and Meunier, Regine and Rohnert, Hans and Sommerlad, Peter and Stal, Michael"
names_last_first__middle_format = "KURSHAN, ROBERT PAUL"
names_last_first__middle_format = "Arden, Wolfgang and Brillou{\"{e}}t, Michel and Cogez, Patrick and Graef, Mart and Huizing, Bert and Mahnkopf, Reinhard and Pelka, Joachim and Pfeiffer, Jens-Uwe and Rouzaud, Andr{\'{e}} and Tartagni, Marco and Hoof, Chris Van and Wagner, Joachim"
names_last_first__middle_format = "Gessner, Thomas and Vogel, Martina and Kaufmann, Christian and Hiller, Karla and Kurth, Steffen and Nestler, J{\"o}rg and Otto, Thomas"
names_last_first__middle_format = "Zhang, Jie and Lin, A. and Patil, N. and Wei, Hai and Wei, Lan and Wong, H.-S. P. and Mitra, S."
names_last_first__middle_format = "Jenney, Joe and Gangl, Mike and Kwolek, Rick and Melton, David and Ridenour, Nancy and Coe, Martin"
names_last_first__middle_format = "Palaniswami, Marimuthu and Attikiouzel, Yianni and {Marks II}, Robert J. and Fogel, David B. and Fukuda, Toshio"
names_last_first__middle_format = "Press, William H. and Teukolsky, Saul A. and Vetterling, William T. and Flannery, Brian P."
names_last_first__middle_format = "Gutin, G. and Johnstone, A. and Reddington, J. and Scott, E. and Soleimanfallah, A. and Yeo, A."
names_last_first__middle_format = "Einwich, Karsten and Grimm, Christoph and Vachoux, Alain and Madrid, Natividad Martinez and Moreno, Felipe Ruiz and Meise, Christian"
names_last_first__middle_format = "Fort, Tomlinson and Graves, Lawrence Murray and MacLane, Saunders and Smith, Paul Althaus"
names_last_first__middle_format = "Grimm, Ch. and Meise, Ch. and Heupke, W. and Waldschmid, K."
names_last_first__middle_format = "Conti, Massimo and Caldari, Marco and Orcioni, Simone and Biagetti, Giorgio"
names_last_first__middle_format = "Barnasconi, Martin and Einwich, Karsten and Grimm, Christoph and Vachoux, Alain"
names_last_first__middle_format = "Einwich, Karsten and Grimm, Christoph and Granig, Wolfgang and Noessing, Gerhard and Scherr, Wolfgang and Scotti, Serge and Barnasconi, Martin and Zucchelli, Giorgia and Vachoux, Alain"
names_last_first__middle_format = "Barnasconi, Martin and Grimm, Christoph and Damm, Markus and Einwich, Karsten and Lou{\"{e}}rat, Marie-Minerve and Maehne, Torsten and Pecheux, Fran{\c{c}}ois and Vachoux, Alain"
names_last_first__middle_format = "Cheung, Eric and Hsieh, Harry and Balarin, Felice"
names_last_first__middle_format = "Bonacina, Maria Paola and Lynch, Christopher A. and de Moura, Leonardo"
names_last_first__middle_format = "Buvat, Jerome and Mehra, Priya and Rao, Tushar and Braunschvig, Benjamin"
names_last_first__middle_format = "Downey, Peter J. and Sethi, Ravi and Tarjan, Robert Endre"
names_last_first__middle_format = "Guimer{\`{a}}, Roger and Sales-Pardo, Marta and Amaral, Lu{\'{i}}s A. N."
names_last_first__middle_format = "Agostinelli, Matteo and Priewasser, Robert and Huemer, Mario and Marsili, Stefano and Straeussnigg, Dietmar"
names_last_first__middle_format = "Alassir, Mohamad and Denoulet, Julien and Romain, Olivier and Garda, Patrick"
names_last_first__middle_format = "Brglez, Franc and Bryan, David and Ko{\'{z}}mi{\'{n}}ski, Krzysztof"
names_last_first__middle_format = "Cimatti, Alessandro and Griggio, Alberto and Sebastiani, Roberto"
names_last_first__middle_format = "Gray, Paul R. and Wooley, Bruce A. and Brodersen, Robert W."
names_last_first__middle_format = "Al-Araji, Saleh R. and Hussain, Zahir M. and Al-Qutayri, Mahmoud A."
names_last_first__middle_format = "Ackroyd, Karen S. and Kinder, Steve H. and Mant, Geoff R. and Miller, Mike C. and Ramsdale, Christine A. and Stephenson, Paul C."
names_last_first__middle_format = "Giusto, Paolo and Martin, Grant and Harcourt, Ed"
names_last_first__middle_format = "Chen, Kaiyu and Malik, Sharad and August, David I."
names_last_first__middle_format = "{Hagel III}, John and Brown, John Seely and Kulasooriya, Duleesha and Elbert, Dan"
names_last_first__middle_format = "Handelsman, Jo and Pfund, Christine and Lauffer, Sarah Miller and Pribbenow, Christine Maidl"
names_last_first__middle_format = "Breuer, Melvin and Chakradhar, Srimat and Joyner, William and Kumar, Rakesh and Raghunathan, Anand and Shanbhag, Naresh and Kurdahi, Fadi and Henkel, J{\"o}rg and Yeh, David"
names_last_first__middle_format = "Fern{\'{a}}ndez, Francisco V. and Rodr{\'{i}}guez-V{\'{a}}zquez, Angel and Huertas, Jos{\'{e}} L. and Gielen, Georges G. E."
names_last_first__middle_format = "Cheng, Chung-Kuan and Qin, Zhanhai and Tan, Sheldon X. D."
names_last_first__middle_format = "Rutenbar, Rob A. and Gielen, Georges G. E. and Roychowdhury, Jaijeet"
names_last_first__middle_format = "Bauer, Andreas and Leucker, Martin and Schallhart, Christian and Tautschnig, Michael"
names_last_first__middle_format = "Densmore, Douglas and {Van Devender}, Anne and Johnson, Matthew and Sritanyaratana, Nade"
names_last_first__middle_format = "Franklin, Gene F. and Powell, J. David and {Emami-Naeini}, Abbas"
names_last_first__middle_format = "{\r{A}}str{\"{o}}m, Karl Johan and Murray, Richard M."
names_last_first__middle_format = "Deliyannis, Theodore L. and Sun, Yichuang and Fidler, J. Kel"
names_last_first__middle_format = "Bandler, John W. and Chen, Shao Hua"
names_last_first__middle_format = "Chandrasekaran, Venkat and Parrilo, Pablo A. and Willsky, Alan S."
names_last_first__middle_format = "Fedder, Gary K. and Howe, Roger T. and Liu, Tsu-Jae King and Qu{\'{e}}vy, Emmanuel P."
names_last_first__middle_format = "Frank, David J. and Puri, Ruchir and Toma, Dorel"
names_last_first__middle_format = "Singer, Maxine F. and Alberts, Bruce M. and Bond, Enriqueta C. and Branscomb, Lewis and Branscomb, Peter and Diamond, Peter and Dinneen, Gerald and Dresselhaus, Mildred S. and Duderstadt, James J. and Fox, Marye Anne and Gomory, Ralph E. and Hearn, Ruby P. and Hogan, Brigid L. M. and Preston, Samuel H. and Shine, Kenneth I. and Tanenbaum, Morris and Weissman, Irving L. and Widnall, Sheila E. and Wilson, William Julius and Wulf, William A."
names_last_first__middle_format = "Gustavsson, Mickael and Wikner, J. Jacob and Tan, Nianxiong Nick"
names_last_first__middle_format = "Huijsing, Johan H. and Steyaert, Michiel and {van Roermund}, Arthur"
names_last_first__middle_format = "Caponetto, Riccardo and Dongola, Giovanni and Fortuna, Luigi and Petr{\'{a}}{\v{s}}, Ivo"
names_last_first__middle_format = "D'Andrea, Raffaello and Dullerud, Geir E."
names_last_first__middle_format = "Brennan, S. and Alleyne, A."
names_last_first__middle_format = "Tsai, Jason Sheng-Hong and Chan, Yu-Pin and Shieh, Leang-San"
names_last_first__middle_format = "Chang, Henry and Kundert, Ken"
names_last_first__middle_format = "Bard, Karen and Dewey, Bill and Hsu, Mei-Ting and Mitchell, Tom and Moody, Karl and Rao, Vasant and Rose, Ron and Soreff, Jeff and Washburn, Steve"
names_last_first__middle_format = "Alpert, Charles J. and Karandikar, Shrirang K. and Li, Zhuo and Nam, Gi-Joon and Quay, Stephen T. and Haoxing Ren, C. N. Sze and Villarrubia, Paul G. and Yildiz, Mehmet C."
names_last_first__middle_format = "Anna W. Topol and Douglas C. {La Tulipe, Jr.} and Leathen Shi and David J. Frank and Kerry Bernstein and Steven E. Steen and Arvind Kumar and Gilbert U. Singco and Albert M. Young and Kathryn W. Guarini and Meikei Leong"
names_last_first__middle_format = "Chu, Chia-Chi and Lai, Ming-Hong and Feng, Wu-Shiung"
names_last_first__middle_format = "Gaff, Brian M. and Toppin, Catherine J."
names_last_first__middle_format = "Bahar, R. Iris and Frohm, Erica A. and Gaona, Charles M. and Hachtel, Gary D. and Macii, Enrico and Pardo, Abelardo and Somenzi, Fabio"
names_last_first__middle_format = "{de Arcangelis}, Lucilla and {Perrone-Capano}, Carla and Herrmann, Hans J."
names_last_first__middle_format = "Alur, R. and Dang, T. and Esposito, J. and Fierro, R. and Hur, Y. and Ivan{\v{c}}i{\'{c}}, F. and Kumar, V. and Lee, I. and Mishra, P. and Pappas, G. and Sokolsky, O."
names_last_first__middle_format = "Goebel, Rafal and Sanfelice, Ricardo G. and Teel, Andrew R."
names_last_first__middle_format = "Akyildiz, Ian F. and Jornet, Josep Miquel"
names_last_first__middle_format = "Atzori, Luigi and Iera, Antonio and Morabito, Giacomo"
names_last_first__middle_format = "Akyildiz, Ian F. and Melodia, Tommaso and Chowdhury, Kaushik R."
names_last_first__middle_format = "Akyildiz, Ian F. and Wang, Xudong and Wang, Weilin"
names_last_first__middle_format = "Akyildiz, I.F. and Su, W. and Sankarasubramaniam, Y. and Cayirci, E."
names_last_first__middle_format = "Akyildiz, Ian F. and Su, Weilian and Sankarasubramaniam, Yogesh and Cayirci, Erdal"
names_last_first__middle_format = "Davis, John H. and Dinn, Neil F. and Falconer, Warren E."
names_last_first__middle_format = "Glossner, John and Iancu, Daniel and Lu, Jin and Hokenek, Erdem and Moudgill, Mayan"
names_last_first__middle_format = "Giannini, Vito and Craninckx, Jan and D'Amico, Stefano and Baschirotto, Andrea"
names_last_first__middle_format = "Getov, Vladimir and Hoisie, Adolfy and Wasserman, Harvey J."
names_last_first__middle_format = "Becker, Tobias and Luk, Wayne and Cheung, Peter Y. K."
names_last_first__middle_format = "Devroye, Natasha and Vu, Mai and Tarokh, Vahid"
names_last_first__middle_format = "Akyildiz, Ian F. and Lee, Won-Yeol and Vuran, Mehmet C. and Mohanty, Shantidev"
names_last_first__middle_format = "Golumbic, Martin Charles and Hartman, Irith Ben-Arroyo"
names_last_first__middle_format = "Bornholdt, Stefan and Schuster, Heinz Georg"
names_last_first__middle_format = "Gupta, Puneet and Kahng, Andrew B. and Kasibhatla, Amarnath and Sharma, Puneet"
names_last_first__middle_format = "Chan, Tony F. and Cong, Jason and Kong, Tianming and Shinnerl, Joseph R."
names_last_first__middle_format = "Cong, Jason and Shinnerl, Joseph R. and Xie, Min and Kong, Tim and Yuan, Xin"
names_last_first__middle_format = "Cong, Jason and Kong, Tim and Shinnerl, Joseph R. and Xie, Min and Yuan, Xin"
names_last_first__middle_format = "Dielacher, Franz and Vogel, Christian and Singerl, Peter and Mendel, Stefan and Wiesbauer, Andreas"
names_last_first__middle_format = "Ferreira, Luis and Batista, Mariano and Fibra, Sebastien and Lee, {Chin Yau} and Silva, Carlos Alexandre Queiroz and Almeida, Joao and Lucchese, Fabiano and Keung, Nam"
names_last_first__middle_format = "Ferreira, Luis and Thakore, Arun and Brown, Michael and Lucchese, Fabiano and RuoBo, Huang and Lin, Linda and Manesco, Paul and Mausolf, Jeff and Momtaheni, Nasser and Subbian, Karthik and Hernandez, Olegario"
names_last_first__middle_format = "Beyer, Hans-Georg and Sendhoff, Bernhard"
names_last_first__middle_format = "Brock, Bishop C. and {Hunt, Jr.}, Warren A. and Kauffmann, Matt"
names_last_first__middle_format = "Jesser, Alexander and Hedrich, Lars and Laemmermann, Stefan and Weiss, Roland and Ruf, Juergen and Kropf, Thomas and Rosenstiel, Wolfgang and Pacholik, Alexander and Fengler, Wolfgang"
names_last_first__middle_format = "Cong, Jason and Lee, John and Luo, Guojie"
names_last_first__middle_format = "Cong, Jason and Lee, John and Vandenberghe, Lieven"
names_last_first__middle_format = "Dabiri, Foad and Nahapetian, Ani and Massey, Tammara and Potkonjak, Miodrag and Sarrafzadeh, Majid"
names_last_first__middle_format = "Chakraborty, Ashutosh and Pan, David Z."
names_last_first__middle_format = "Bhardwaj, Sarvesh and Vrudhula, Sarma"
names_last_first__middle_format = "Hanchate, Narender and Ranganathan, Nagarajan"
names_last_first__middle_format = "Alpert, Charles J. and Chu, Chris and Villarrubia, Paul G."
names_last_first__middle_format = "Cong, Jason and Gupta, Puneet and Lee, John"
names_last_first__middle_format = "Dutt, Shantanu and Ren, Huan"
names_last_first__middle_format = "Gu, Chenjie and Roychowdhury, Jaijeet"
names_last_first__middle_format = "Alipour, Salar and Hidaji, Babak and Pour, Amir Sabbagh"
names_last_first__middle_format = "Fujimoto, Kenji and Scherpen, Jacquelien M. A."
names_last_first__middle_format = "Narendra, Siva G. and Chandrakasan, Anantha"
names_last_first__middle_format = "Ganai, Malay K. and Gupta, Aarti"
names_last_first__middle_format = "Barkalov, Alexander and Titarenko, Larysa"
names_last_first__middle_format = "Cios, Krzysztof J. and Pedrycz, Witold and Swiniarski, Roman W. and Kurgan, Lukasz A."
names_last_first__middle_format = "Chatterjee, Shouri and Pun, {Kong Pang} and Stani{\'{c}}, Neboj{\v{s}}a and Tsividis, Yannis and Kinget, Peter"
names_last_first__middle_format = "Bourdi, Taoufik and Kale, Izzet"
names_last_first__middle_format = "Breuer, L. and Baum, D."
names_last_first__middle_format = "Foster, Harry D. and Krolnik, Adam C."
names_last_first__middle_format = "Eisner, Cindy and Fisman, Dana"
names_last_first__middle_format = "Hager, William W. and Huang, Shu-Jen and Pardalos, Panos M. and Prokopyev, Oleg A."
names_last_first__middle_format = "Bonnans, J. Fr{\'{e}}d{\'{e}}ric and Gilbert, J. Charles and Lemar{\'{e}}chal, Claude and Sagastiz{\'{a}}bal, Claudia A."
names_last_first__middle_format = "Brummitt, Charles D. and D'Souza, Raissa M. and Leicht, E. A."
names_last_first__middle_format = "Singhee, Amith and Rutenbar, Rob A."
names_last_first__middle_format = "di Bernardo, Mario and Champneys, Alan R. and Budd, Christopher J. and Kowalczyk, Piotr"
names_last_first__middle_format = "Brin, Michael and Stuck, Garrett"
names_last_first__middle_format = "G{\"{o}}ssel, Michael and Ocheretny, Vitaly and Sogomonyan, Egor and Marienfeld, Daniel"
names_last_first__middle_format = "Rutenbar, Rob A. and Cohn, John M."
names_last_first__middle_format = "Fritzson, Peter and Cellier, Fran{\c{c}}ois and Nytsch-Geusen, Christoph"
names_last_first__middle_format = "Ausl{\"{a}}nder, Simon and Ausl{\"{a}}nder, David and M{\"{u}}ller, Marius and Wieland, Markus and Fussenegger, Martin"
names_last_first__middle_format = "Bawazer, Lukmaan A. and Izumi, Michi and Kolodin, Dmitriy and Neilson, James R. and Schwenzer, Birgit and Morse, Daniel E."
names_last_first__middle_format = "Balint, Adrian and Belov, Anton and Diepold, Daniel and Gerber, Simon and J{\"{a}}rvisalo, Matti and Sinz, Carsten"
names_last_first__middle_format = "Grady, Daniel and Thiemann, Christian and Brockmann, Dirk"
names_last_first__middle_format = "Cidon, Asaf and London, Tomer"
names_last_first__middle_format = "Barrett, Chris and Eubank, Stephen and Marathe, Madhav"
names_last_first__middle_format = "Blank, Steve and Dorf, Bob"
names_last_first__middle_format = "Fried, Jason and Hansson, David Heinemeier"
names_last_first__middle_format = "Beeby, Stephen and White, Neil"
names_last_first__middle_format = "Bailey, Brian and Martin, Grant"
names_last_first__middle_format = "Bose, Pradip and Conte, Thomas M."
names_last_first__middle_format = "Eyre, Jennifer and Bier, Jeff"
names_last_first__middle_format = "Wilson, Janet and Tremblay, Marc and Grohoski, Greg and Burgess, Brad and Killian, Earl and Colwell, Robert P. and Rubinfeld, Paul I."
names_last_first__middle_format = "Ishikawa, Masatoshi and McArdle, Neil"
names_last_first__middle_format = "Carreira, Joao and Silva, Joao Gabriel"
names_last_first__middle_format = "Mitkas, Pericles A. and Betzos, George A. and Irakliotis, Leo J."
names_last_first__middle_format = "Clark, David D. and Feigenbaum, Edward A. and Hartmanis, Juris and Lucky, Robert W. and Metcalfe, Robert M. and Reddy, Raj and Shaw, Mary"
names_last_first__middle_format = "Goodrich, Michael T. and Tamassia, Roberto and Mount, David M."
names_last_first__middle_format = "Liu, {Yang-Yu} and Slotine, {Jean-Jacques} and Barab{\'{a}}si, Albert-L{\'{a}}szl{\'{o}}"
names_last_first__middle_format = "Cachin, Christian and Guerraoui, Rachid and Rodrigues, Lu{\'{i}}s"
names_last_first__middle_format = "Mattson, Timothy G. and Sanders, Beverly A. and Massingill, Berna L."
names_last_first__middle_format = "Carnevale, Anthony P. and Cheah, Ban and Strohl, Jeff"
names_last_first__middle_format = "Chakrabarty, Krishnendu and Iyengar, Vikram and Chandra, Anshuman"
names_last_first__middle_format = "Chakrabarty, Krishnendu and Zeng, Jun"
names_last_first__middle_format = "Bahukudumbi, Sudarshan and Chakrabarty, Krishnendu"
names_last_first__middle_format = "Chakrabarty, Krishnendu and Iyengar, S. S."
names_last_first__middle_format = "Cafaro, Massimo and Aloisio, Giovanni"
names_last_first__middle_format = "Baun, Christian and Kunze, Marcel and Nimis, Jens and Tai, Stefan"
names_last_first__middle_format = "Deschamps, {Jean-Pierre} and Ima{\~{n}}a, Jos{\'{e}} Luis and Sutter, Gustavo D."
names_last_first__middle_format = "Hwang, Kai and Xu, Zhiwei"
names_last_first__middle_format = "Leupers, Rainer and Marwedel, Peter"
names_last_first__middle_format = "Barnasconi, Martin and Einwich, Karsten and Grimm, Christoph and Maehne, Torsten and Vachoux, Alain"
names_last_first__middle_format = "Stephen L. Campbell and Meyer, Carl D."
names_last_first__middle_format = "Downey, R. G. and Fellows, M. R."
names_last_first__middle_format = "Garey, Michael R. and Johnson, David S."
names_last_first__middle_format = "Jackson, Phil and Delehanty, Hugh"
names_last_first__middle_format = "Ismail, Mohammed and Franca, Jos{\'{e}}"
names_last_first__middle_format = "Alpert, Charles and Li, Zhuo and Nam, {Gi-Joon} and Sze, C. N. and Viswanathan, Natarajan and Ward, Samuel I."
names_last_first__middle_format = "Chuang, {Yi-Lin} and Nam, {Gi-Joon} and Alpert, Charles J. and Chang, {Yao-Wen} and Roy, Jarrod and Viswanathan, Natarajan"
names_last_first__middle_format = "Drechsler, Rolf and Eggersgl{\"{u}}{\ss}, Stephan and Fey, G{\"{o}}rschwin and Tille, Daniel"
names_last_first__middle_format = "Larson, Ron and Falvo, David C."
names_last_first__middle_format = "Gandy, R. O. and Yates, C. E. M."
names_last_first__middle_format = "{\v{C}}iegis, Raimondas and Henty, David and K{\r{a}}gstr{\"{o}}m, Bo and {\v{Z}}ilinskas, Julius"
names_last_first__middle_format = "Alves, Carlos J. S. and Pardalos, Panos M. and Vicente, Luis Nunes"
names_last_first__middle_format = "Chinchuluun, Altannar and Pardalos, Panos M. and Migdalas, Athanasios and Pitsoulis, Leonidas"
names_last_first__middle_format = "Grimmett, Geoffrey R. and Stirzaker, David R."
names_last_first__middle_format = "Lipschutz, Seymour and Lipson, Marc Lars"
names_last_first__middle_format = "Barclay, Kenneth and Savage, John"
names_last_first__middle_format = "Dally, William J. and Poulton, John W."
names_last_first__middle_format = "Aarts, Emile and Lenstra, Jan Karel"
names_last_first__middle_format = "Tsividis, Yannis and {McAndrew}, Colin"
names_last_first__middle_format = "Bening, Lionel and Foster, Harry"
names_last_first__middle_format = "Gray, Robert M."
names_last_first__middle_format = "Halloway, Stuart and Bedra, Aaron"
names_last_first__middle_format = "Churiwala, Sanjay and Garg, Sapan"
names_last_first__middle_format = "Yuan, Fei and Opal, Ajoy"
names_last_first__middle_format = "Celik, Mustafa and Pileggi, Lawrence and Odabasioglu, Altan"
names_last_first__middle_format = "G{\"{a}}rtner, Bernd and Matou{\v{s}}ek, Ji{\v{r}}{\'{i}}"
names_last_first__middle_format = "Pardalos, Panos M. and Wolkowicz, Henry"
names_last_first__middle_format = "Blekherman, Grigoriy and Parrilo, Pablo A. and Thomas, Rekha R."
names_last_first__middle_format = "Pellerin, David and Thibault, Scott"
names_last_first__middle_format = "Densmore, Douglas and Hassoun, Soha"
names_last_first__middle_format = "Rodriguez, Claudia Salzberg and Fischer, Gordon and Smolski, Steven"
names_last_first__middle_format = "Martelli, Alex and Ravenscroft, Anna Martelli and Ascher, David"
names_last_first__middle_format = "Goyvaerts, Jan and Levithan, Steven"
names_last_first__middle_format = "Albing, Carl and Vossen, {J. P.} and Newham, Cameron"
names_last_first__middle_format = "Adelstein, Tom and Lubanovic, Bill"
names_last_first__middle_format = "Darte, Alain and Robert, Yves and Vivien, Fr{\'{e}}d{\'{e}}ric"
names_last_first__middle_format = "Pukite, Jan and Pukite, Paul"
names_last_first__middle_format = "Bernardo, Marco and Degano, Pierpaolo and Zavattaro, Gianluigi"
names_last_first__middle_format = "Grune, Dick and Jacobs, Ceriel J. H."
names_last_first__middle_format = "Begain, Khalid and Bolch, Gunter and Herold, Helmut"
names_last_first__middle_format = "Br{\"{a}}unl, Thomas and Feyrer, Stefan and Rapf, Wolfgang and Reinhardt, Michael"















print(f"Current list of names:{names_last_first__middle_format}=")

"""
	Use a character space as the delimiter between entities in the list of names.

	Names of different co-authors are separated by " and ".

	Names of each (co-)author, such as their first/given name, family/surname, or middle name, are separated by a character space.

	There are (co-)authors with compound surnames, such as double/double-barrelled/hyphenated/triple-barrelled surnames, or some other compound surname (such as those that contain nobiliary particles to reflect the nobility of their family or family name affixes).

	There are (co-)authors with compound given names.

	Also, there are (co-)authors that have their names written only in lower case.

	The names are statistically not going to be in all lower case.
	For a significant number of times, they appear in all upper case.

	+ For tokens that have only one alphabetical character, keep this character as an initial of the name.
"""

"""
	Placeholder for list of names in the following format.

	[family name (or surname)], [given name or its initial] [optional middle name(s) or initials of middle names]
"""
names_first_to_last_format = ""

# Delmit tokens in the list of names with " and ".
tokenized_names = names_last_first__middle_format.split(" and ")
# Enumerate the list of tokens obtained from the list of names.
for index, current_name in enumerate(tokenized_names):
	# Delimit the full name based on a comma, ",".
	tokenized_current_name = current_name.split(",")
	"""
		Since people have name suffixes that are generational
			(i.e., generational titles), such as "Sr." and "Jr."
			or "II" and "III", we assume that the last comma in the
			full name refers to the separating comma between the
			family name (or surname) and the given name (or its
			initial).

		Checking for multiple commas in the name is redundant,
			since the last token contains the names or initials
			of the first/given name (and middle names, if any).

		Hence, the name in the desired format is to obtain
			the last element of the list, followed by appending
			the previous elements without the last comma.
	
		Since I do not need to use "temp_name" anymore,
			I can destory it.
		Instead of using tokenized_current_name[-1] or
			tokenized_current_name[len(tokenized_current_name)-1]
			to access the last token, pop/remove the last token
			from the list and assign it to temp_name.

		Since names with multiple commas should have all by the
			last comma preserved, I am appending a comma to the
			addition of each token to preserve the commas.
	"""
	temp_name = tokenized_current_name.pop()
	for name_component in tokenized_current_name:
		temp_name += " "
		temp_name += name_component
		temp_name += ","
	"""
		Since this results in the name having an unwanted comma
			at the end, delete the last character of the name.
	"""
	temp_name = temp_name[:-1]
	names_first_to_last_format += temp_name
	# Are there are more names to process?
	if index != (len(tokenized_names) - 1):
		# Yes. Add " and " to delimit these names.
		names_first_to_last_format += " and"
		print(">>	Current name in the list,",temp_name,"=")
	# Else, do nothing.
print(f"Fixed list of names:{names_first_to_last_format}=")

"""
	The result is:
	Eric R. Keiter and Thomas V. Russo and Richard L. Schiek and Peter E. Sholander and Heidi K. Thornquist and Ting Mei and Jason C. Verley and David G. Baur
"""