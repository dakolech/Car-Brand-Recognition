#!/bin/bash
out_dir="vec_samples"

rm -r -f $out_dir
mkdir $out_dir
num=$1
out="$num"_samples.vec
xangle=0.2
yangle=0.2
zangle=0.1
perl ../createtrainsamples.pl positive_list negative_list $out_dir $num "opencv_createsamples  -bgcolor 0 -bgthresh 0 -maxxangle $xangle -maxyangle yangle maxzangle zangle -maxidev 40 -w 25 -h 25"

files=`ls -1 $out_dir | grep .jpg`
vec_list="$out_dir/vectors.list"

for file in $files;do
	echo  "./$out_dir/$file">>$vec_list	
done;

../opencv_mergevec $vec_list $out

