#!/usr/bin/python
# -*- coding: utf-8 -*-

from vector import Vector

class Wave(object):
    myDebug = None
    theta = None
    thetaDelta = None
    centerX = None
    centerY = None
    waveLength = None
    color = None
    speed = None
    direction = None

    def __init__(self, debug, direction, theta, thetaDelta, cX, cY, len, col, speed):
    	self.myDebug = debug
    	self.direction = direction
    	self.theta = float(theta)
    	self.thetaDelta = float(thetaDelta)
    	self.centerX = int(cX)
    	self.centerY = int(cY)
    	self.waveLength = float(len)
    	self.color = col
    	self.speed = float(speed)
    
    def getValue(self, x, y):
        """
        Returns the value of the wave at the given x y coordinate
        
        @param x: the x coordinate
        @param y: the y coordinate
        @return: the value of the wave between -1 and 1
        """
        raise NotImplementedError()
        
    def update(self):
        """
        Moves the wave one time step
        """
        self.theta += self.thetaDelta
        
    def getColor(self):
        """
        Returns the color value of the wave
        
        @return: The 3 tuple of R,G,B values
        """
        return self.color


