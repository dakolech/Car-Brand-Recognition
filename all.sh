#!/bin/bash

for i in `ls samples|head -n $1`;do
	./classify.py samples/$i
done