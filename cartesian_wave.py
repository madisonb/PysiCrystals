#!/usr/bin/python
# -*- coding: utf-8 -*-

from wave import Wave
from vector import Vector
import math

class CartesianWave(Wave):

    def __init__(self, myDebug, direction, theta, thetaDelta, cX, cY, len, color, speed):
        Wave.__init__(self, myDebug, direction, theta, thetaDelta, cX, cY, len, color, speed)
        
    def getValue(self, x, y):
        # project point (x, y) onto vector
        v1 = Vector(x - self.centerX, y - self.centerY)
        # vector
        p = v1.project(self.direction);
        # adjust so the point is correct
        p.x += self.centerX
        p.y += self.centerY
        # get the vector from the point to (x, y)
        d = Vector(x - p.x, y - p.y)
        l = d.length()
							
        # normal of current vector
        n = Vector(self.direction.y, -self.direction.x)
						
        # adjust for sign on each side of the vector
        p = v1.dot(n)
        sign = 1
        if p > 0:
            sign = -1
						
        #print math.sin(self.theta + sign * l / self.waveLength)
        return math.sin(self.theta + sign * l / self.waveLength);
        
