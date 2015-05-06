# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 12:26:11 2015

@author: Wasit
"""
import numpy as np
def partition(k,n):
    p1=np.ones(n%k,dtype=int)*(n/k+1)
    p2=np.ones(k-n%k,dtype=int)*(n/k)
    p=np.concatenate((p1,p2))
    #print p
    return p
if __name__ == "__main__":
    #number of element of data
    n=14
    #number of cores
    k=3
    p=partition(k,n)
    print p