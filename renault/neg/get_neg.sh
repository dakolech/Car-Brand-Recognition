#!/bin/bash

files=`ls -1 | grep .jpg`
out="../negative_list"
rm $out
for file in $files;do
	echo "./neg/$file">>$out	
done;