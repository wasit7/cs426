# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:45:42 2015

@author: Wasit
"""
#parallel
import time
import numpy as np
from six.moves import zip
from bokeh.plotting import *

def part(n=20, m=3):
    base = n//m;
    extra = n-m*(n//m)
    #loads is list of number of tasks per core
    loads=np.ones(m,dtype=np.int32)*base
    loads[0:extra]=base+1
    #taskboundary is the list  of starting element of each task
    tb = [0]
    c = 0
    for load in loads:
        tb.append(tb[c] +load)
        c+=1  
    return tb
    
    
if __name__ == "__main__":    
    N = 20    
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
    
    ##create parallel clients
    from IPython import parallel 
    c = parallel.Client(packer='pickle') 
    c.block = True 
    print(c.ids)  
    ##create direct view 
    dview = c.direct_view() 
    dview.block = True
    
    dview.execute("import b_engine as be")
    M=len(c.ids)
    boundary=part(N,M)
    while True:
        print sx[0]
        ## transfer data to engines
        dview['sx']=sx
        dview['sy']=sy
        dview['vx']=vx
        dview['vy']=vy
        dview['m']=m
        #call transition function
        for i in xrange(M):            
            c[i].execute("sxk,syk,vxk,vyk = be.transition(sx,sy,vx,vy,m,%d,%d)"%(boundary[i],boundary[i+1]))
            
        ## gather results back to controller    
        sx=dview.gather('sxk')
        sy=dview.gather('syk') 
        vx=dview.gather('vxk')
        vy=dview.gather('vyk')               
        ds.data["x"] = sx
        ds.data["y"] = sy
        cursession().store_objects(ds)
        #time.sleep(0.01)