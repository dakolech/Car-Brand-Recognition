#!/bin/bash
dir="training_out"
rm -r -f $dir/*
posNum=`cat ./positive_list |wc -l`
negNum=`cat ./negative_list |wc -l`
vecFile="pos.vec"
wh=25
let posNum=$posNum-1
ftype="LBP"
stages=15
ftype="HAAR"
#posnum=199
#vecFile="single.vec"

opencv_traincascade -data $dir -vec $vecFile -bg negative_list -numPos $posNum -numNeg $negNum -numStages $stages -w $wh -h $wh -featureType $ftype -precalcValBufSize 2048 -precalcIdxBufSize 2048