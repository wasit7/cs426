# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 03:21:34 2015

@author: Wasit
"""
import pickle
from sctree import tree
import numpy as np
import codecs

with open('root.pic', 'rb') as pickleFile:
    root = pickle.load(pickleFile)
    
#init the test tree
t=tree()
t.settree(root)
t.show()

pattern=np.zeros(10,dtype=np.int32)
p=t.classify(pattern)
newtext=unicode("")
mincode=3585
for i in xrange(100):
    nextchar=p.argsort()[::-1][0]
    newtext+=unichr( nextchar + mincode)
    pattern=np.roll(pattern,-1)
    pattern[-1]=nextchar
    p=t.classify(pattern)

print 'writing text'
with codecs.open("test.txt", "w", "utf-8-sig") as textFile:
    textFile.write(newtext)
    
    