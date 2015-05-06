# -*- coding: utf-8 -*-
"""
Created on Wed Feb 04 12:08:44 2015

@author: Wasit
"""
from IPython import parallel
c = parallel.Client(packer='pickle')
c.block = True
print(c.ids)

##create direct view
dview = c.direct_view()
dview.block = True
print(dview)
gN_total=4000000

#begin parallel

dview.execute('N_total=%d'%(gN_total))
dview.run('N_in.py')
gN_in = dview.gather('N_in')
#end parallel

import numpy as np
pi=float(np.sum(gN_in))*4.0/float(len(c.ids)*gN_total)
print pi

