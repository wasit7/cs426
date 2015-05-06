# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 11:09:33 2015

@author: Wasit
"""
import numpy as np
def myfunction(x):
    n=0
    for i in xrange(1000000):
        n=n+i
    print mysubfuction(1000)
    return np.sum(x)
def mysubfuction(c):
    n=0
    for i in xrange(c):
        n=n+i
    return n
#always execute
if __name__ == "__main__":
    #only main process execute
    x=np.arange(1e6)
    y=myfunction(x)
    a=np.arange(1e7)
    b=myfunction(a)
    print y
    print b