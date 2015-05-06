# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 10:08:58 2015

@author: Wasit
"""

import numpy as np
import matplotlib.pyplot as plt
#from IPython import parallel

#c=parallel.Client()
#print c.ids
#dv=c.direct_view()

sx=np.random.rand(10)*2.0-1.0
sy=np.random.rand(10)*2.0-1.0

plt.plot(sx,sy,'.b')

#plt.axis([-1,1,-1,1])