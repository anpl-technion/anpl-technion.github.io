#!/bin/sh

# generate publications per research topics that appear in the file ResearchTopics.txt
cd research-projects-bib

#remove previous files
rm pubs-*.*

bibfilename="../VadimIndelman"
while IFS= read -r line; do
    currentresearch=$line
    outputfile="pubs-$currentresearch"
    echo $outputfile
    #echo "START - $outputfile-Journals.html"
    
    # generate bib file that only contains bib-entries with the current research topic	
	python python/filter_bib_by_entry_type.py $bibfilename $outputfile researchtopic $currentresearch
	
done <../ResearchTopics.txt		

