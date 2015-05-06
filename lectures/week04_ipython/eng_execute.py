# -*- coding: utf-8 -*-
"""
Created on Wed Feb 04 11:37:50 2015

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
dview.execute('import numpy as np')
dview.execute('N_total=%d'%(gN_total))
dview.execute('x=np.random.rand(N_total)')
dview.execute('y=np.random.rand(N_total)')
dview.execute('d_sq=x*x+y*y')
dview.execute('N_in=np.sum(d_sq<1.0)')
gN_in = dview.gather('N_in')
#end parallel

import numpy as np
pi=float(np.sum(gN_in))*4.0/float(len(c.ids)*gN_total)
print pi
