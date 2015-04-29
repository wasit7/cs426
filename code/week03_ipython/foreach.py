# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:48:06 2015

@author: Wasit
"""
from IPython import parallel
c = parallel.Client(packer='pickle')
c.block = True
print(c.ids)

for i in xrange(len(c.ids)):
    print i
    c[i].execute("f=open('m%03d.txt','w')"%(i))
