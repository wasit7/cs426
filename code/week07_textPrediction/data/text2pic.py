# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 00:16:17 2015

@author: Wasit
"""

import codecs
import pickle
import numpy as np

theta_range=10 #lenth of characters used for prediction
N=100
I=[]
samples=[]
mincode=3585
maxcode=3675
clmax=maxcode-mincode
theta_dim=1
with codecs.open("text.txt", "r", "utf-8-sig") as textFile:
        alltext=textFile.read()
        
for i,x in enumerate(np.random.randint(theta_range,len(alltext)-theta_range-1,N)):
    curChar=ord(alltext[x+theta_range])            
    if mincode<curChar and curChar<=maxcode:  
        samples.append(curChar)        
        I.append(map(ord,alltext[x:x+theta_range]))
samples=np.array(samples)-mincode
I=np.array(I)-mincode
print I
print len(samples)

print 'writing pickle'
with open('data.pic', 'wb') as pickleFile:
    pickle.dump((clmax,theta_dim,theta_range,len(samples),samples,I,None), pickleFile, pickle.HIGHEST_PROTOCOL)

print 'reading pickle'
with open('data.pic', 'rb') as pickleFile:
    clmax,theta_dim,theta_range,size,samples,I,unused_pos = pickle.load(pickleFile)


sampleText=''
for i in xrange(len(samples)):
    sampleText+=(
    reduce(lambda x,y:x+y,map(unichr,I[i,:]+mincode))
    +unichr(samples[i]+mincode)
    +"\r\n")
print 'writing text'
with codecs.open("samples.txt", "w", "utf-8-sig") as textFile:
    textFile.write(sampleText)