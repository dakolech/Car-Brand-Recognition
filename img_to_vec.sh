#!/bin/bash

in_file=$1
in_file2="negative_list"
out="single.vec"
samples=200

xangle=2
yangle=2
zangle=2
dev=50
wh=25
show="-show"
show=""

opencv_createsamples  -bgcolor 0 -bg negative_list -img $in_file -num $samples -vec $out -h $wh -w $wh $show -maxxangle $xangle -maxyangle $yangle -maxzangle $zangle -maxidev $dev