# -*- coding: utf-8 -*-
"""
Created on Thu Sep 03 18:01:21 2015

@author: Wasit
"""

####test ipython.parallel
# to start ipcluster use
# $ipcluster start -n 4﻿

##create clients
import numpy as np
from IPython import parallel
c = parallel.Client(packer='pickle')
c.block = True
print(c.ids)

##create direct view
dview = c.direct_view()
dview.block = True
print(dview)

dview.execute('import numpy as np')

##using execute
dview.execute('a=np.random.randint(0,5,size=(1,2))')
print("a:\n{}".format(dview.gather('a')))

##using run
f=open('iptest.py','w')
f.write('import numpy as np\nb=np.zeros(shape=(1,4),dtype=np.int32)')
f.close()
dview.run('iptest.py')
print("b:\n{}".format(dview.gather('b')))
print type(dview.gather('b')[0,0])

##using dictionary
dview['c']=np.ones(shape=(2,3),dtype=np.int8)
print("a:\n{}".format(dview.gather('c')))
print type(dview.gather('c')[0,0])