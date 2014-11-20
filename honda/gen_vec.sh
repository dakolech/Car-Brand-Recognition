#!/bin/bash
out_dir="vec_samples"

rm -r $out_dir
mkdir $out_dir
../createtrainsamples.pl positive_list negative_list $out_dir 200 "opencv_createsamples  -bgcolor 0 -bgthresh 0 -maxxangle 1.1 -maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w 25 -h 25"