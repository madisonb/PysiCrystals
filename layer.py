#!/usr/bin/python
# -*- coding: utf-8 -*-

from cartesian_wave import CartesianWave
from polar_wave import PolarWave

class Layer(object):
    numWaves = None
    rounding = None
    perWave = None
    
    def __init__(self):
        pass
        
    def getValue(self, x, y):
        """
        Get the value of the layer at that particular pixel
        
        @param x: the x coordinate
        @param y: the y coordinate
        @return: the value of this layer at x, y  between 0 and 1
        """
        pass


