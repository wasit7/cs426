# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 11:27:40 2015

@author: Wasit
"""

#import numpy as np
import matplotlib.pyplot as plt

#init
s=1.0
v=0.0
a=0.0
k=1.0
dt=0.1
m=1.0


plt.close('all')
plt.ion()
while 1:
    #transition
    a=-k*s/m
    v=v+a*dt
    s=s+v*dt
    #display
    plt.plot(0,s,'.k')    
    plt.hold(False)
    plt.axis([-2,2,-2,2])
    plt.draw()
