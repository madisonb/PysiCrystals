#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import argparse
from layer import Layer
import ConfigParser
from debug import Debug
from PIL import Image

config = ConfigParser.SafeConfigParser()
confString = 'pysi'
myDebug = None
layers = []

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('config_file', help='configuration file to load')
    parser.add_argument('output_file', help='output filename')
    args = vars(parser.parse_args())
    
    configFile = args['config_file']
    outputFile = args['output_file']
    
    if os.path.isfile(configFile):
        with open(configFile) as cf:
            config.readfp(cf)
    else:
        print("Could not find the configuration file specified.")
        sys.exit()

    type = None   
    width = None
    height = None 
    try:
    	debugEnabled = config.get(confString, 'debug')
    	myDebug = Debug(debugEnabled)
        type = config.get(confString, 'type')
        myDebug.dprint("Config file type: " + str(type))
    	
    	if type == 'basic':
    	    waves = int(config.get(confString, 'waves'))
    	    color = config.get(confString, 'color')
    	    coords = config.get(confString, 'coords')
    	    waveLength = int(config.get(confString, 'wavelength'))
    	    speed = int(config.get(confString, 'speed'))
    	    width = int(config.get(confString, 'width'))
    	    height = int(config.get(confString, 'height'))
    	    myDebug.dprint("Configuration read successfully")
    	    
    	    l = Layer(myDebug)
    	    l.initBasic(waves, color, .3, coords, speed, waveLength, width, height)
    	    layers.append(l)
    	    
    	elif type == 'advanced':
    	    pass
    	elif type == 'layered':
    	    pass
    	elif type == 'vectors':
    	    pass
    	else:
            print("Unknown config file type: " + str(type))
            sys.exit()

    except ConfigParser.NoOptionError:
        print("Not all parameters specified for type: " + str(type))
        sys.exit()
        
    image = Image.new("RGB", (width, height))
    pix = image.load()
    print(image.size)
    for x in range(width):
        for y in range(height):
            for i in range(len(layers)):
                layer = layers[i]
                val = layer.getValue(x, y)
                val[0] = int(val[0])
                val[1] = int(val[1])
                val[2] = int(val[2])
                #myDebug.dprint("layer val: " + str(val))
                pix[x, y] = tuple(val)
                
    image.save(outputFile)




