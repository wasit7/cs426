# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 12:51:13 2015

@author: arsen_000
"""

import numpy as np
import matplotlib.pyplot as plt


N = 100
s = np.random.rand(N,2)*20-10
r = np.zeros((2,N,N))*20-10
epsilon = 1e-4
m = 10.0
G = 1
v = np.zeros((N,2))
dt = 0.01
radious=0.1

while True :    
    for i in xrange (N):
        for j in xrange (N):
            r[:,i,j] = s[j,:] - s[i,:]
    
    
    c = (r[0,:,:]**2 + r[1,:,:]**2 + epsilon**2)**(-1.5)
    a = r*c
    np.fill_diagonal(a[0,:,:], 0)
    np.fill_diagonal(a[1,:,:], 0)
    ai=np.transpose( G * m * np.sum(a,axis=2) )
    v = v + ai*dt

    s = s + v*dt
    
    plt.plot(s[:,0],s[:,1],'.r')
    plt.hold(False)
    plt.axis([-20,20,-20,20])
    plt.draw()
