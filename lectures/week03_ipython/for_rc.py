# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:57:31 2015

@author: Wasit
"""
import numpy as np
rs=range(0,5)
cs=range(0,5)
p=[]
for r in rs:
    for c in cs:
        p.append((r,c))
p=np.array(p)
##create clients
from IPython import parallel
c = parallel.Client(packer='pickle')
c.block = True
print(c.ids)

##create direct view
dview = c.direct_view()
dview.block = True
print(dview)
