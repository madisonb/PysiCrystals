#!/usr/bin/python
# -*- coding: utf-8 -*-

class Debug(object):

    isEnabled = None
    
    def __init__(self, enab):
        """
        @param enab: True or False for verbose/debugging 
        """
        self.isEnabled = enab
        
    def dprint(self, string):
        """
        Prints a string to the command line
        """
        if self.isEnabled:
            print(string)
            
    def enabled(self):
        return self.isEnabled
