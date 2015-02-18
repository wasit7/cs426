# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 09:46:35 2015

@author: Wasit
"""
def transition(sx,sy,vx,vy):
    m=1.0
    dt=0.1
    k=1.0
    # Newton's second law f=ma
    #Hooke's Law f=-ks
    #Therefore a=-ks/a
    ax=-k*sx/m
    ay=-k*sy/m
    
    vx=vx+ax*dt
    vy=vy+ay*dt
    
    sx=sx+vx*dt
    sy=sy+vy*dt
    return sx,sy,vx,vy
    
    print "transition"


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    import time

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
        plt.hold(False)
        plt.axis([-1,1,-1,1])
        plt.draw()
        time.sleep(0.1)

