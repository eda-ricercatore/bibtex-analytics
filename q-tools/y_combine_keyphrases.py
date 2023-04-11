#!/usr/local/bin/python3

a_string = ""

"""
	Does not work for files with keyphrases that have double quotes.
"""


#with open("./input-files/keyphrases.md") as file_obj:
with open("/Users/zhiyang/Documents/ricerca/saag-bibtex/outputs/scripts/input-files/keyphrases.md") as file_obj:
	#all_lines = file_obj.readline()
	for cur_line in file_obj:
		a_string = a_string + cur_line.rstrip() + ", "
#a_string = "fact-shopping, US people - fact-shopping, alternative universe, fake news, fake news websites, fake/biased news, false information, misinformation, disinformation, alternative facts, alternative news cycle, alternate realities, weapons of mass deception, doctored data, doctored experimental data, falsified evidence, falsified experimental data, manufactured facts, fabricated facts, fabricated experimental data, selective exposure theory, selective exposure, card stacking, stacking the deck, ignoring the counterevidence, slanting, suppressed evidence, suppressing evidence, cherry picking, fallacy of incomplete evidence, echo chamber, circular sourcing, Dunning-Kruger effect, one-sided argument, 1-sided argument, handpicked & cultivated & meticulously packaged arguments, doublespeak, uses of fear, fear+uncertainty+doubt, fear appeals, fear mongering, fear of vulnerability, fear-based crisis management, poorly vetted ideas, misleading statistics, data-saturated world, art of skepticism, skepticism, healthy skepticism, cynicism, obfuscations, deliberate obfuscations, careless obfuscations, personal bias, personal bias confirmation, social sorting, unintentional discriminatory practices, personalized filtering, biased information, misleading information, Balkanize the Net, Realpolitik, hoax news websites, false flag, gaslighting, half-truth, hoax, Internet manipulation, media manipulation, Potemkin village, Potyomkin village, post-reality politics, smear campaign, smear tactic, smear, social bot, socialbot, socbot, spin (propaganda), spin doctors, spinmeisters, whataboutism, whataboutery, dumbing down, bothsidesism, Machiavellianism, Orwellian, psychological manipulation, sircular reporting false confirmation, alternative facts, deplatforming, no-platforming, speech error, slip of the tongue, misspeaking, junk news, pseudo-news, deception, catachresis, thought-terminating cliche, semantic stop-signs, thought-stoppers, cliche thinking, transfer (propaganda), argument maps, argument diagrams, ideograph (rhetoric), virtue word, historical revisionism, indoctrination, lawfare, loaded terms, emotive language, high-inference language, language-persuasive techniques, Newspeak, obscurantism, propaganda of the deed, propaganda by the deed, rally 'round the flag effect, rally 'round the flag syndrome, weasel word, anonymous authority, Aesopian language, polite fiction, manipulative abuse, cognitive distortion, exculpatory information, information overload, infobesity infoxication, information anxiety, information explosion, propaganda, computational propaganda, spread of fake/biased news using social media, loaded language, social psychology, persuasion, social cognition, person perception, propaganda on social media, propaganda through media, media bias in the United States, media bias, coverage bias, visibility bias, gatekeeping bias, selectivity, selection bias, agenda bias, statement bias, tonality bias, presentation bias, corporate bias, mainstream bias, partisan bias, sensationalism, structural bias, newsworthiness, half-truths, partial-truths, hoaxes, confirmation bias, post-truth politics, post-factual politics"
print("a_string is:",a_string,"=")

b_list = a_string.split(", ")
print("Length of b_list is:",len(b_list),"=")
c_set = set(b_list)
print("Length of c_set is:",len(c_set),"=")
for x in b_list:
	if b_list.count(x) > 1:
		print("x is:",x,"=")




d_list = "MapReduce, MapReduce frameworks, MapReduce paradigm, MapReduce processing, data sharing, data sharing systems, resilient distributed data sets, RDDs, Spark programming model, Spark stack, fault tolerance, fault tolerance in distributed systems, fault-tolerant architectures, fault-tolerant computing, fault-tolerant computer systems, fault-tolerant computer architecture, fault-tolerant distributed systems, fault-tolerant systems, data analytics, SQL, Structured Query Language, machine learning, machine learning algorithms, iterative algorithms, batch processing, data processing, data processing systems, distributed computer systems, distributed computing, distributed computer architectures".split(", ")
e_set = set(d_list)
f_list = "cluster computing, data processing, data processing systems, distributed systems, machine learning, graph analysis, streaming multiprocessors, batch processing, computing platforms, fault tolerance, 1-pass computations, multi-pass algorithms, iterative algorithms, data analytics, data analysis, big data, big data analysis, MapReduce, MapReduce programming model, resilient distributed data sets, RDDs, data sets, Apache Spark (cluster computing), fault-tolerant systems, fault-tolerant computing".split(", ")
g_set = set(f_list)
h_set = e_set.union(g_set)
print("Length of e_set is:",len(e_set),"=")
print("Length of g_set is:",len(g_set),"=")
print("Length of h_set is:",len(h_set),"=")
h_set_to_list = list(h_set)


i_list = ""
for x in h_set:
	i_list = i_list + ", " + x
	#i_list = x + ", " + i_list
print("i_list is:",i_list,"=")
#	data sharing systems, MapReduce programming model, big data analysis, big data, machine learning algorithms, fault tolerance in distributed systems, distributed computer architectures, MapReduce paradigm, batch processing, Apache Spark (cluster computing), MapReduce processing, distributed systems, streaming multiprocessors, fault-tolerant computing, fault-tolerant computer architecture, cluster computing, 1-pass computations, Structured Query Language, SQL, Spark programming model, fault-tolerant architectures, fault-tolerant computer systems, iterative algorithms, data sets, multi-pass algorithms, graph analysis, data sharing, data analytics, resilient distributed data sets, Spark stack, distributed computer systems, machine learning, RDDs, data analysis, fault tolerance, MapReduce, data processing systems, distributed computing, fault-tolerant distributed systems, data processing, computing platforms, fault-tolerant systems, MapReduce frameworks


"""
	Merge list 

	Reference:
	+ https://stackoverflow.com/questions/1720421/how-do-i-concatenate-two-lists-in-python
		- https://stackoverflow.com/a/35631185/1531728
		- https://stackoverflow.com/questions/1720421/how-do-i-concatenate-two-lists-in-python/35631185#35631185
		- Dimitris Fasarakis Hilliard and Boris Verkhovskiy, Answer to "How do I concatenate two lists in Python?," Stack Exchange Inc., New York, NY, November 22, 2019. Available online from *Stack Exchange Inc.: Stack Overflow: Questions* at: https://stackoverflow.com/a/35631185/1531728 and https://stackoverflow.com/questions/1720421/how-do-i-concatenate-two-lists-in-python/35631185#35631185; March 25, 2021 was the last accessed date.
"""
j_merged_list = d_list + f_list
k_merged_set = set(j_merged_list)
l_list = ""
for x in k_merged_set:
	l_list = l_list + ", " + x
print("l_list is:",l_list,"=")
#	distributed systems, iterative algorithms, fault-tolerant systems, data sharing systems, fault tolerance in distributed systems, distributed computing, resilient distributed data sets, fault-tolerant computer architecture, multi-pass algorithms, fault-tolerant distributed systems, MapReduce processing, distributed computer architectures, fault-tolerant architectures, batch processing, graph analysis, fault-tolerant computer systems, streaming multiprocessors, cluster computing, Spark stack, Apache Spark (cluster computing), data processing, big data analysis, data sets, RDDs, Spark programming model, fault-tolerant computing, computing platforms, data sharing, MapReduce paradigm, data analysis, distributed computer systems, 1-pass computations, data processing systems, MapReduce programming model, MapReduce, fault tolerance, data analytics, machine learning algorithms, SQL, big data, MapReduce frameworks, Structured Query Language, machine learning

#	Cannot subtract a list from another to get their differences.
#diff_lists = j_merged_list - h_set_to_list
diff_sets = k_merged_set - h_set
print("diff_sets is:",diff_sets,"=")
print("Length of k_merged_set is:",len(k_merged_set),"=")
print("Length of h_set is:",len(h_set),"=")