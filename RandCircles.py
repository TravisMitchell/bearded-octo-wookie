"""
Created on Fri Apr 08 11:02 2016

@author: uqtmitc3

Randomly generated circles - for use in multiphase
models to create initial conditions of distributed
bubbles - inputs take domain (NX x NY) as well as 
the number of bubbles (nbubbles) and the size of t
hem (radius).

"""
import random

def RandCircles(NX,NY,nbubbles,radius):
    r      = int(2*radius)
    rangeX = (2*radius, NX-2*radius)
    rangeY = (2*radius, NY-2*radius)
    n      = nbubbles
    
    delta  = set()
    for x in range(-r, int(r+1)):
        for y in range(-r, int(r+1)):
            if x*x + y*y <= r*r:
                delta.add((x,y))
                
    randPoints  = []
    excluded    = set()
    i = 0
    while i < n:
        x = random.randrange( *rangeX )
        y = random.randrange( *rangeY )
        if (x,y) in excluded:
            #print "skipped invalid point"
            continue
        randPoints.append((x,y))
        i += 1
        excluded.update((x+dx, y+dy) for (dx,dy) in delta)
	print "\n Circle Found"
#    for i in range(n):
#        print randPoints[i]
#    print excluded
    return randPoints
    
if __name__=="__main__":
    randPoints= RandCircles(100,100,40,2)
    #import matplotlib.pyplot as plt
    #plt.plot(randPoints,'b.')
    #plt.show()
