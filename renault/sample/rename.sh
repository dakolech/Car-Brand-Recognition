#!/bin/bash

brand=$1
i=0
for photo in `ls -1 *jpg`;do
	mv $photo "$brand-$i.jpg"
	let i=$i+1
done  