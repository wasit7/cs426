# -*- coding: utf-8 -*-
"""
TSV dataset generator

Created on Wed Aug 26 01:50:45 2015

@author: Wasit
"""

import csv
import numpy as np
N=100
pos=np.random.random([2,N])*100
A=np.zeros([N,N])
for r in xrange(N):
    for c in xrange(r+1,N):
        A[r,c]=np.linalg.norm(pos[:,r]-pos[:,c])
        A[c,r]=A[r,c]
with open('data2.tsv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([N])
    for r in xrange(N):   
        writer.writerow(A[r,:])