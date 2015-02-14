# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 14:51:20 2015

@author: Wasit
"""

def mean(x):
    sum=0.0;
    for xi in x:
        sum=sum+xi
    return sum/len(x)

def variance(x):
    xbar=mean(x)
    sum=0.0;
    for xi in x:
        sum=sum+(xi-xbar)**2
    return sum/len(x)
def std(x):
    return variance(x)**0.5
if __name__ == "__main__":
    import numpy as np
    mu, sigma = 0, 0.1 # mean and standard deviation
    x = np.random.normal(mu, sigma, 1000000)
    print mean(x)
    print std(x)