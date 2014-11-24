#!/bin/bash

for i in `ls samples/* -1`;do
	./classify.py $i
done