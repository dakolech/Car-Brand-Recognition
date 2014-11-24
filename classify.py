#!/usr/bin/env python

import cv2
import sys
import numpy as np
# Get user supplied values
def numToBrand(n):
	if n==-1:
		return "Can't say"
	if n==0:
		return "Honda"
	if n==1:
		return "Citroen"
	if n==2:
		return "Renault"
	if n==3:
		return "Mercedes"
	if n==4:
		return "Opel"

def pickBestResult(results,neibs,treshold=6):
	best=(0,0)
	for r,n in zip(results,neibs):
		curval=0
		for i in n:
			if r[0]==i:
				curval+=1
		if curval>best[1]:
			best=(r[0],curval)
	if best[1]>treshold:
		return best[0]
	else:
		return -1

cascPath="cascades/"
# Create the haar cascade
hondaCascade = cv2.CascadeClassifier(cascPath+"honda.xml")
mercedesCascade = cv2.CascadeClassifier(cascPath+"mercedes.xml")
renaultCascade = cv2.CascadeClassifier(cascPath+"renault.xml")
citroenCascade = cv2.CascadeClassifier(cascPath+"citroen.xml")
opelCascade = cv2.CascadeClassifier(cascPath+"opel.xml")
# Read the image
imagePath = sys.argv[1]

image = cv2.imread(imagePath)
w=image.shape[1]

scale=1000.0/w
image=cv2.resize(image,(0,0),fx=scale,fy=scale)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# prepare images for knn
hondas=[]
for i in range(1,44):
	filepath="positives/honda"+str(i)+".jpg"
	im=cv2.imread(filepath)
	w=im.shape[1]
	scalex=25.0/w
	w=im.shape[0]
	scaley=25.0/w
	im=cv2.resize(im,(0,0),fx=scalex,fy=scaley)
	im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	hondas.append(im)
citroens=[]
for i in range(1,26):
	filepath="positives/citroen-"+str(i)+".jpg"
	im=cv2.imread(filepath)
	w=im.shape[1]
	scalex=25.0/w
	w=im.shape[0]
	scaley=25.0/w
	im=cv2.resize(im,(0,0),fx=scalex,fy=scaley)
	im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	citroens.append(im)
mercedeses=[]
for i in range(1,26):
	filepath="positives/Mercedes-"+str(i)+".jpg"
	im=cv2.imread(filepath)
	w=im.shape[1]
	scalex=25.0/w
	w=im.shape[0]
	scaley=25.0/w
	im=cv2.resize(im,(0,0),fx=scalex,fy=scaley)
	im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	mercedeses.append(im)
renaults=[]
for i in range(1,31):
	filepath="positives/renault-"+str(i)+".jpg"
	im=cv2.imread(filepath)
	w=im.shape[1]
	scalex=25.0/w
	w=im.shape[0]
	scaley=25.0/w
	im=cv2.resize(im,(0,0),fx=scalex,fy=scaley)
	im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	renaults.append(im)
opels=[]
for i in range(1,38):
	filepath="positives/opel"+str(i)+".jpg"
	im=cv2.imread(filepath)
	w=im.shape[1]
	scalex=25.0/w
	w=im.shape[0]
	scaley=25.0/w
	im=cv2.resize(im,(0,0),fx=scalex,fy=scaley)
	im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	opels.append(im)

train=[]
labels=[]
for car in hondas:
	labels.append([0])
	train.append(car)
for car in citroens:
	labels.append([1])
	train.append(car)
for car in renaults:
	labels.append([2])
	train.append(car)
for car in mercedeses:
	labels.append([3])
	train.append(car)
for car in opels:
	labels.append([4])
	train.append(car)


# Detect objects in the image
hondas = hondaCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(20, 20),
    #maxSize=(70,70),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)
citroens = citroenCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(20, 20),
    #maxSize=(70,70),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)
renaults = renaultCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(20, 20),
    #maxSize=(70,70),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)
mercedeses = mercedesCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(20, 20),
    #maxSize=(70,70),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)
opels=[]

opels = opelCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(20, 20),
    #maxSize=(70,70),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)







#find logos

found=[];
for (x, y, w, h) in hondas:
	cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
	im=image[y:y+h,x:x+w]
	w=im.shape[1]
	scalex=25.0/w
	w=im.shape[0]
	scaley=25.0/w
	im=cv2.resize(im,(0,0),fx=scalex,fy=scaley)
	im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	found.append(im)
	
for (x, y, w, h) in mercedeses:
	cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
	im=image[y:y+h,x:x+w]
	w=im.shape[1]
	scalex=25.0/w
	w=im.shape[0]
	scaley=25.0/w
	im=cv2.resize(im,(0,0),fx=scalex,fy=scaley)
	im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	found.append(im)
for (x, y, w, h) in citroens:
	cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 255), 2)
	im=image[y:y+h,x:x+w]
	w=im.shape[1]
	scalex=25.0/w
	w=im.shape[0]
	scaley=25.0/w
	im=cv2.resize(im,(0,0),fx=scalex,fy=scaley)
	im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	found.append(im)
for (x, y, w, h) in renaults:
	cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)
	im=image[y:y+h,x:x+w]
	w=im.shape[1]
	scalex=25.0/w
	w=im.shape[0]
	scaley=25.0/w
	im=cv2.resize(im,(0,0),fx=scalex,fy=scaley)
	im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	found.append(im)
for (x, y, w, h) in opels:
	cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
	im=image[y:y+h,x:x+w]
	w=im.shape[1]
	scalex=25.0/w
	w=im.shape[0]
	scaley=25.0/w
	im=cv2.resize(im,(0,0),fx=scalex,fy=scaley)
	im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	found.append(im)






train=np.array(train).reshape(-1,625).astype(np.float32)
found=np.array(found).reshape(-1,625).astype(np.float32)

labels=np.array(labels)
knn = cv2.KNearest()
knn.train(train,labels)

brandNum=0;
if found.shape[0]>0:
	if found.shape[0]==len(hondas):
		brandNum=0
	elif found.shape[0]==len(citroens):
		brandNum=1
	elif found.shape[0]==len(renaults):
		brandNum=2
	elif found.shape[0]==len(mercedeses):
		brandNum=3
	elif found.shape[0]==len(opels):
		brandNum=4
	else:
		ret,results,neighbours,dist = knn.find_nearest(found,k=10)
		#print "result: ", results,"\n"
		#print "neighbours: ", neighbours,"\n"
		#print "distance: ", dist
		brandNum=pickBestResult(results,neighbours,5)
		
else:
	brandNum=-1

print imagePath+": "+numToBrand(brandNum)
#cv2.imshow("Car brand detection", image)
#cv2.waitKey(0)
