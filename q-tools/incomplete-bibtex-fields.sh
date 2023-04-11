#!/bin/zsh



cd /Users/zhiyang/Documents/ricerca/saag-bibtex/outputs/scripts
cat -n ../../references.bib | grep  "Title = {"  | grep   -v "},"
cat -n ../../references.bib | grep  "Keywords = {"  | grep   -v "},"
cat -n ../../references.bib | grep  "Address = {"  | grep   -v "},"
cat -n ../../references.bib | grep  "Author = {"  | grep   -v "},"
cat -n ../../references.bib | grep  "Booktitle = {"  | grep   -v "},"
cat -n ../../references.bib | grep  "Chapter = {"  | grep   -v "},"
cat -n ../../references.bib | grep  "Doi = {"  | grep   -v "},"
cat -n ../../references.bib | grep  "Edition = {"  | grep   -v "},"
cat -n ../../references.bib | grep  "Editor = {"  | grep   -v "},"
cat -n ../../references.bib | grep  "Howpublished = {"  | grep   -v "},"
cat -n ../../references.bib | grep  "Institution = {"  | grep   -v "},"
cat -n ../../references.bib | grep  "Journal = {"  | grep   -v "},"
cat -n ../../references.bib | grep  "Month = {"  | grep   -v "},"
cat -n ../../references.bib | grep  "Number = {"  | grep   -v "},"
cat -n ../../references.bib | grep  "Organization = {"  | grep   -v "},"
cat -n ../../references.bib | grep  "Pages = {"  | grep   -v "},"
cat -n ../../references.bib | grep  "Publisher = {"  | grep   -v "},"
cat -n ../../references.bib | grep  "School = {"  | grep   -v "},"
cat -n ../../references.bib | grep  "Series = {"  | grep   -v "},"
cat -n ../../references.bib | grep  "Url = {"  | grep   -v "},"  | grep   -v "}}"
cat -n ../../references.bib | grep  "Volume = {"  | grep   -v "},"
cat -n ../../references.bib | grep  "Year = {"  | grep   -v "},"  | grep   -v "}}"
#cat -n ../../references.bib | grep  "Annote = {"  | grep   -v "},"
cd /Users/zhiyang/Documents/ricerca/saag-bibtex
incomplete_entries.py references.bib








# Known problems
#	Title = {All The Words I Should Have Said}}
#	Title = {How to Ace Interview Questions}}
#	Title = {The Ultimate Guide To {TCK} Living: Understanding The World Around You}}
#	Title = {Race Matters in College}}
#	Title = {Public Funding Observatory 2020/2021 -- Part 1: Financial and economic impact of the Covid-19 
#	Howpublished = {Available online from {\it Computing Research Association: Computing Community Consortium: Resources: {CCC}-Led White Papers} at: \url{http://cra.org/ccc/docs/init/bigdatawhitepaper.pdf}; July 5, 2012 was the last accessed date},

