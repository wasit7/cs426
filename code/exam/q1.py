# -*- coding: utf-8 -*-
"""
Created on Mon May 25 09:01:43 2015

@author: Wasit
"""
import numpy as np
import pickle
pfile=open('q1_input.pic','wb')
A=np.random.rand(5000,8000)
B=np.random.rand(8000,9000)
pickle.dump((A,B),pfile,pickle.HIGHEST_PROTOCOL)
pfile.close()