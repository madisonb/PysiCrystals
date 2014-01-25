#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

class Vector(object):

    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def dot(self, v2)
	    return self.x * v2.x + self.y * v2.y;
		
	def length(self)
        return math.sqrt(self.x * self.x + self.y * self.y)
		
	def project(self, b)
		proj = Vector(0, 0)
		val = self.dot(b) / b.dot(b)
		proj.x = val * b.x
		proj.y = val * b.y
		return proj

