# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 09:46:35 2015

@author: Wasit
"""
def transition(sx,sy,vx,vy):
    m=1.0
    dt=0.01
    G=0.1
    epsilon=1e-6
    # http://http.developer.nvidia.com/GPUGems3/gpugems3_ch31.html
    
    for i in xrange(len(sx)):
        ax_i=0.0;
        ay_i=0.0;
        for j in xrange(len(sx)):
            if i!=j:
                rx_ij=sx[j]-sx[i]
                ry_ij=sy[j]-sy[i]
                f=(rx_ij**2 + ry_ij**2 + epsilon*2)**-1.5
                ax_i=ax_i + G*m*rx_ij*f
                ay_i=ay_i + G*m*ry_ij*f
            
        vx[i] = vx[i] + ax_i*dt
        vy[i]  =vy[i] + ay_i*dt
        
    sx = sx + vx*dt
    sy = sy + vy*dt
    return sx,sy,vx,vy
    
    print "transition"


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    #init particle
    N=100
    sx=np.random.rand(N)*2.0-1.0
    sy=np.random.rand(N)*2.0-1.0
    vx=np.zeros(N)
    vy=np.zeros(N)
    
    plt.close('all')
    fig = plt.figure()
    plt.plot(sx,sy,'.b')
    plt.hold(False)
    plt.axis([-1,1,-1,1])
    while 1:        
        #call transition function
        (sx,sy,vx,vy) = transition(sx,sy,vx,vy)
        
        #display
        plt.plot(sx,sy,'.b')
        plt.hold(True)
        #plt.plot(sx[0],sy[0],'.r')
        plt.hold(False)
        plt.axis([-2,2,-2,2])
        plt.draw()

