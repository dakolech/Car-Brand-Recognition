#!/bin/bash

for i in `ls sample`;do
	./detect.py sample/$i
done