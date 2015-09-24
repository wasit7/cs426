# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 02:00:00 2015

@author: Wasit
"""

import codecs
import pickle
import numpy as np
import os

theta_range=10 #lenth of characters used for prediction
N=100000
mincode=3585
maxcode=3675
clmax=maxcode-mincode
theta_dim=1
Ncores=8
target_dir="../parallel_forest/training/"
if not os.path.exists(target_dir):
    os.makedirs(target_dir)
    
with codecs.open("text.txt", "r", "utf-8-sig") as textFile:
        alltext=textFile.read()
for j in xrange(Ncores): 
    I=[]
    samples=[]
    for i,x in enumerate(np.random.randint(theta_range,len(alltext)-theta_range-1,N)):
        curChar=ord(alltext[x+theta_range])            
        if mincode<curChar and curChar<=maxcode:  
            samples.append(curChar)        
            I.append(map(ord,alltext[x:x+theta_range]))
    samples=np.array(samples)-mincode
    I=np.array(I)-mincode
    
    path=os.path.join(target_dir,'dataset%02d.pic'%(j))
    print 'writing pickle to %s'%path
    with open(path, 'wb') as pickleFile:
        pickle.dump((clmax,theta_dim,theta_range,len(samples),samples,I,None), pickleFile, pickle.HIGHEST_PROTOCOL)