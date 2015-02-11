# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 11:46:23 2015

@author: Wasit
"""
import numpy as np
from IPython import parallel
from k_partition import partition
c=parallel.Client()
dv=c.direct_view()
print c.ids

x = np.linspace(0, 7, 8)
y = np.linspace(0, 7, 8)
B, A = np.meshgrid(x, y)

#dv.scatter('a',yv)
#dv.scatter('b',xv.transpose())
#dv.execute('c=np.dot(a,b.transpose())')

#rmax is a number of row of the output matrix
rmax=A.shape[0]

#cmax is a number of column of the output matrix
cmax=B.shape[1]

r_par=4
c_par=2
pr=partition(r_par,rmax)
pc=partition(c_par,cmax)
ri=0
for i in xrange(r_par):    
    rf=ri+pr[i]    
    c[i*c_par:(i+1)*c_par]['a']=A[ri:rf,:]
    
    print 'core ',i*c_par,':',(i+1)*c_par
    print 'row ',ri,':',rf
    ri=rf
print dv['a']