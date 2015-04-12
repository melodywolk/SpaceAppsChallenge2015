#!/bin/bash

# Create a csv table of possible impacts of all objects. 
# Excute: ./get_riskObj.sh OUTPUT
# Need Larry's program, scrape.pl, which graps possible of impact of one object
# PFW 2015.04.11

touch $1

wget http://neo.jpl.nasa.gov/risks/
less index.html | grep .html | grep nowrap | awk -F '=' '{print $2}' | awk -F '.' '{print $1}' > tmp

cat tmp | while read line
do
 ./scrape.pl $line > foo
 echo $line
 less foo | awk 'NR>=2' >> $1
 rm -f foo 
done

rm -f index.html
rm -f tmp
