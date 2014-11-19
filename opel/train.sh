#!/bin/bash
dir="training_out"
rm -r -f $dir/*
posNum=`cat ./positive_list |wc -l`
negNum=`cat ./negative_list |wc -l`
wh=40
let posNum=$posNum-1
ftype="LBP"
stages=15
ftype="HAAR"


opencv_traincascade -data $dir -vec pos.vec -bg negative_list -numPos $posNum -numNeg $negNum -numStages $stages -w $wh -h $wh -featureType $ftype -precalcValBufSize 2048 -precalcIdxBufSize 2048