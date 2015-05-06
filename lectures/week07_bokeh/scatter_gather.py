# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:17:42 2015

@author: Wasit
"""

from IPython import parallel
import numpy as np
c = parallel.Client(packer='pickle') 
c.block = True 
print(c.ids)

##create direct view 
dview = c.direct_view() 
dview.block = True 

x=np.arange(20)
print 'x=%s'%x

dview.scatter('x_eng',x)
x_con=dview.gather('x_eng')
