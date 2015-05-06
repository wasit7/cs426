# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 11:46:23 2015

@author: Wasit
"""
import numpy as np
from IPython import parallel
from k_partition import partition
c=parallel.Client()
print c.ids
dv=c.direct_view()
dv.execute('import numpy as np')


x = np.linspace(0, 7, 8)
y = np.linspace(0, 7, 8)
B, A = np.meshgrid(x, y)


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
    x=i*c_par+np.arange(c_par) 
    for j in x:
        c[j]['a']=A[ri:rf,:]
    print 'core: ',x
    print 'row ',ri,':',rf
    ri=rf
#print dv['a']

ci=0
for i in xrange(c_par):    
    cf=ci+pc[i]
    x=np.arange(r_par)*c_par+i
    for j in x:
        c[j]['b']=B[:,ci:cf]
    
    print 'core: ',x
    print 'column ',ci,':',cf
    ci=cf
#print dv['b']
dv.execute('c=np.dot(a,b)')