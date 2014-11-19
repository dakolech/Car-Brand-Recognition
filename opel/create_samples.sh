#!/bin/bash

in_file="positive_list"
out="pos.vec"
samples=`cat $in_file |wc -l`
wh=40

opencv_createsamples -info $in_file -num $samples -vec $out -h $wh -w $wh