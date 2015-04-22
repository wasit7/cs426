# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:45:42 2015

@author: Wasit
"""

import time
import numpy as np
from six.moves import zip
from bokeh.plotting import *

def part(n=20, m=3):
    base = n//m;
    extra = n-m*(n//m)
    x=np.ones(m,dtype=np.int32)*base
    x[0:extra]=base+1
    y = [0]
    c = 0
    for i in x:
        y.append(y[c] +i)
        c+=1  
    return y
    
    
if __name__ == "__main__":    
    N = 150  
    sx = np.random.random(size=N) * 100
    sy = np.random.random(size=N) * 100
    vx = np.zeros(shape=N)
    vy = np.zeros(shape=N)
    m=np.random.random(size=N)
    
    colors = ["#%02x%02x%02x" % (r, g, 150) for r, g in zip(np.floor(50+2*sx), np.floor(30+2*sy))]
    
    TOOLS="resize,crosshair,pan,wheel_zoom,box_zoom,reset,tap,previewsave,box_select,poly_select,lasso_select"
    
    #output_file("color_scatter.html", title="color_scatter.py example")
    #output_server("scatter_animate", url='http://10.200.30.55:5006/')
    output_server("scatter_animate")
    
    p = figure(tools=TOOLS)
    p.scatter(sx,sy, radius=m, fill_color=colors, fill_alpha=0.6, line_color=None,name="particles")
    
    show(p)  # open a browser
    #get renderer from object by tag name
    renderer = p.select(dict(name="particles"))
    #data from object
    ds = renderer[0].data_source
    
    import b_engine as be
    while True:
        print sx[0]
        sx,sy,vx,vy = be.transition(sx,sy,vx,vy,m,0,N)              
        ds.data["x"] = sx
        ds.data["y"] = sy
        cursession().store_objects(ds)
        #time.sleep(0.01)