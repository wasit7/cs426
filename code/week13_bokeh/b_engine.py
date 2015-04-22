# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:46:41 2015

@author: Wasit
"""
import numpy as np
def transition(sx,sy,vx,vy,m,start=0,stop=3):
    dt=0.5
    G=1.0
    epsilon=1e0
    # http://http.developer.nvidia.com/GPUGems3/gpugems3_ch31.html
    sxk=sx[start:stop]
    syk=sy[start:stop]
    vxk=vx[start:stop]
    vyk=vy[start:stop]
    axk=np.zeros(stop-start)
    ayk=np.zeros(stop-start)
    for k,i in enumerate(xrange(start,stop)):
        for j in xrange(len(sx)):
            if i!=j:
                rx_ij=sx[j]-sx[i]
                ry_ij=sy[j]-sy[i]
                f=(rx_ij**2 + ry_ij**2 + epsilon*2)**-1.5
                axk[k]=axk[k] + G*m[i]*rx_ij*f
                ayk[k]=ayk[k] + G*m[i]*ry_ij*f
                
    vxk=vxk+axk*dt
    vyk=vyk+ayk*dt    
    sxk = sxk + vxk*dt
    syk = syk + vyk*dt
    return sxk,syk,vxk,vyk

if __name__=="__main__": 
    sx=np.arange(0,10)
    sy=np.arange(10,0,-1)
    vx=np.zeros(10)
    vy=np.zeros(10)
    m=np.ones(10)
    start=0
    stop=3
    _sx,_sy,_vx,_vy=transition(sx,sy,vx,vy,m,0,3)
#    dt=1
#    G=0.1
#    epsilon=1e0
#    # http://http.developer.nvidia.com/GPUGems3/gpugems3_ch31.html
#    sxk=sx[start:stop]
#    syk=sy[start:stop]
#    vxk=vx[start:stop]
#    vyk=vy[start:stop]
#    axk=np.zeros(stop-start)
#    ayk=np.zeros(stop-start)
#    for k,i in enumerate(xrange(start,stop)):
#        for j in xrange(len(sx)):
#            if i!=j:
#                rx_ij=sx[j]-sx[i]
#                ry_ij=sy[j]-sy[i]
#                f=(rx_ij**2 + ry_ij**2 + epsilon*2)**-1.5
#                axk[k]=axk[k] + G*m[i]*rx_ij*f
#                ayk[k]=ayk[k] + G*m[i]*ry_ij*f
#                
#    vxk=vxk+axk*dt
#    vyk=vyk+ayk*dt    
#    sxk = sxk + vxk*dt
#    syk = syk + vyk*dt