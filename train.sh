#!/bin/bash
dir="training_out"
rm -r -f $dir
mkdir $dir
rm -r -f $dir/*
vecFile=$1
posNum=$2-1

negNum=`cat ./negative_list |wc -l`
wh=25
stages=15
ftype="HAAR"
#posnum=199
#vecFile="single.vec"

opencv_traincascade -data $dir -vec $vecFile -bg negative_list -numPos $posNum -numNeg $negNum -numStages $stages -w $wh -h $wh -featureType $ftype -precalcValBufSize 2048 -precalcIdxBufSize 2048