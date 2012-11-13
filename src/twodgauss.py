"""
Module for fitting 2d Gaussians to things.
"""

import numpy as n

def moments(data):
    total = n.abs(data).sum()
    Y,X = n.indices(data.shape)
    y = n.argmax((X*n.abs(data)).sum(axis=1)/total)
    x = n.argmax((Y*n.abs(data)).sum(axis=0)/total)
    col = data[int(y),:]
    row = data[:,int(x)]
    #First moment.
    width_x = n.sqrt(n.abs((n.arange(col.size)-y)*col).sum()/n.abs(col).sum())
    width_y = n.sqrt(n.abs((n.arange(row.size)-x)*row).sum()/n.abs(row).sum())
    width = ( width_x + width_y ) / 2.
    height = n.median(data.ravel())
    amplitude = data.max() - height
    mylist = [amplitude,x,y]
    if n.isnan(width_y) or n.isnan(width_x) or n.isnan(height) or n.isnan(amplitude):
        raise ValueError("Somehthing is nan")
    mylist = [height] + mylist
    mylist = mylist + [width_x,width_y]
    return mylist

def twodgaussian(inpars,shape=None):
    inpars_old = inpars
    inpars = list(inpars)
    height = inpars.pop(0)
    height = float(height)
    amplitude,center_y,center_x = inpars.pop(0),inpars.pop(0),inpars.pop(0)
    amplitude = float(amplitude)
    center_x = float(center_x)
    center_y = float(center_y)
    width_x,width_y = inpars.pop(0),inpars.pop(0)
    rcen_x = center_x
    rcen_y = center_y
    if len(inpars) > 0:
        raise ValueError("There are still input parameters:" + str(inpars) + \
                        " and you've input: " + str(inpars_old) + \
                        " circle=%d, rotate=%d, vheight=%d" % (circle,rotate,vheight) )
    def rotgauss(x,y):
        xp = x
        yp = y
        #g = amplitude*n.exp( 
        #    -(((rcen_x-xp)/width_x)**2 + 
        #    ((rcen_y-yp)/width_y)**2)/2.)
        g = n.exp( 
            -(((rcen_x-xp)/width_x)**2 + 
            ((rcen_y-yp)/width_y)**2)/2.)
        g /= (2*n.pi*width_x*width_y)

        return g
    if shape is not None:
        return rotgauss(*n.indices(shape))
    else:
        return rotgauss
