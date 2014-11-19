#!/bin/bash

in_file="positive_list"
out="pos.vec"
samples=`cat $in_file |wc -l`
let samples=$samples
maxangle=10
wh=40
show="-show"
show=""
opencv_createsamples -info $in_file -num $samples -vec $out -h $wh -w $wh -maxxangle $maxangle -maxyangle $maxangle -maxzangle $maxangle $show