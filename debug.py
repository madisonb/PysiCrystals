#!/usr/bin/python
# -*- coding: utf-8 -*-

class Debug(object):

    enabled = None
    
    def __init__(self, enab):
        """
        @param enab: True or False for verbose/debugging 
        """
        self.enabled = enab
        
    def dprint(self, string):
        """
        Prints a string to the command line
        """
        if self.enabled:
            print(string)
