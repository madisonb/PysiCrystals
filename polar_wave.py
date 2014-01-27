#!/usr/bin/python
# -*- coding: utf-8 -*-

from wave import Wave
import math
from vector import Vector

class PolarWave(Wave):

    def __init__(self, myDebug, direction, theta, thetaDelta, cX, cY, len, color, speed):
        Wave.__init__(self, myDebug, direction, theta, thetaDelta, cX, cY, len, color, speed)

    def getValue(self, x, y):
        # log polar coordinates
        theta2 = math.atan2(self.direction.y,self.direction.x); 
        r = math.log(self.direction.length());
        return math.cos((theta2 * self.direction.x - r * self.direction.y) + self.theta); 



