#!/bin/bash

files=`ls -1 | grep .jpg`
out="../positive_list"
rm $out
for file in $files;do
	echo -n "./pos/$file 1 0 0 ">>$out	
 	identify $file|cut -f 3 -d " "|tr "x" " ">>$out
done;