#!/usr/bin/python
# -*- coding: utf-8 -*-

from vector import Vector

class Wave(object):

    theta = None
    thetaDelta = None
    centerX = None
    centerY = None
    waveLength = None
    color = None

    def __init__(self):
        pass
    
    def getValue(self, x, y):
        """
        Returns the value of the wave at the given x y coordinate
        
        @param x: the x coordinate
        @param y: the y coordinate
        @return: the value of the wave between 0 and 1
        """
        raise NotImplementedError()
        
    def update(self):
        """
        Moves the wave one time step
        """
        theta += thetaDelta
        
    def getColor(self):
        """
        Returns the color value of the wave
        
        @return: The 3 tuple of R,G,B values
        """
        return self.color


