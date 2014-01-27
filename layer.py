#!/usr/bin/python
# -*- coding: utf-8 -*-

from cartesian_wave import CartesianWave
from polar_wave import PolarWave
import math
from vector import Vector

class Layer(object):
    numWaves = None
    rounding = None
    perWave = None
    myDebug = None
    waves = []
    
    def __init__(self, debug):
        self.myDebug = debug
        pass
        
    def initBasic(self, numWaves, colorType, tD, coords, speed, len, width, height):
        start = 0
        stop = math.pi * 3
        step = stop / numWaves
        self.myDebug.dprint("Creating basic layer waves")
        while start < stop:
            vec = Vector(math.cos(start), math.sin(start))
            wave = None
            if coords == 'cartesian':
                wave = CartesianWave(self.myDebug, vec, 0, tD, width / 2,
                                     height / 2, len, (256, 256, 256), speed)
            else:
                wave = PolarWave(self.myDebug, vec, 0, tD, width / 2, 
        	                     height / 2, len, (256, 256, 256), speed)
            self.waves.append(wave)
            start += step
        
    def getValue(self, x, y):
        """
        Get the value of the layer at that particular pixel
        
        @param x: the x coordinate
        @param y: the y coordinate
        @return: the value of this layer's color in a list between 0 and 256 for RGB
        """
        nWaves = len(self.waves)
        perWave = 1.0 / nWaves
        color = [0.0, 0.0, 0.0]
        for i in range(nWaves):
            wave = self.waves[i]
            col = wave.getColor()
            val = wave.getValue(x, y)
            #print col[0] , val , perWave
            color[0] += col[0] * val * perWave
            color[1] += col[1] * val * perWave
            color[2] += col[2] * val * perWave
            #print col
            #print color
        return color
                
    def update(self):
        """
        Updates the waves one iteration
        """
        for i in range(nWaves):
            self.waves[i].update()


