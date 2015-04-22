# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 12:51:13 2015

@author: arsen_000
"""

import numpy as np
import matplotlib.pyplot as plt


N = 100
s = np.random.rand(N,2)*2-1
r = np.zeros((2,N,N))*2-1
v = np.zeros((N,2))

m=1.0
dt=0.01
G=0.1
epsilon=1e-3
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


'''
    # check collision
    for i in xrange (N):
        for j in xrange (N):
            if i!=j and r[0,i,j]**2 + r[1,i,j]**2<radious**2:
                vbar=0.5*(v[i,:]+v[j,:])
                v[i,:]=vbar
                v[j,:]=vbar
                s[i,:]=s[j,:]
'''