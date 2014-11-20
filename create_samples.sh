#!/bin/bash

in_file="positive_list"
in_file2="negative_list"
out="pos.vec"
samples=`cat $in_file |wc -l`
let samples=$samples
xangle=5
yangle=5
zangle=5
dev=100
wh=25
show="-show"
show=""

opencv_createsamples  -info $in_file -num $samples -vec $out -h $wh -w $wh  $show 