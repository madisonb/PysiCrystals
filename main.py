#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import argparse
from layer import Layer
import ConfigParser
from debug import Debug
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time
from images2gif import writeGif

config = ConfigParser.SafeConfigParser()
confString = 'pysi'
VERSION = '0.5'
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
    frames = None
    duration = None
    try:
    	debugEnabled = config.get(confString, 'debug')
    	myDebug = Debug(debugEnabled)
        type = config.get(confString, 'type')
        myDebug.dprint("Config file type: " + str(type))
    	
    	if type == 'basic':
    	    waves = int(config.get(confString, 'waves'))
    	    color = config.get(confString, 'color')
    	    coords = config.get(confString, 'coords')
    	    waveLength = float(config.get(confString, 'wavelength'))
    	    speed = float(config.get(confString, 'speed'))
    	    width = int(config.get(confString, 'width'))
    	    height = int(config.get(confString, 'height'))
    	    td = float(config.get(confString, 'delta'))
    	    frames = int(config.get(confString, 'frames'))
    	    duration = float(config.get(confString, 'time'))
    	    myDebug.dprint("Configuration read successfully")
    	    
    	    l = Layer(myDebug)
    	    l.initBasic(waves, color, td, coords, speed, waveLength, width, height)
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
        
    images = []
    oldTime = None
    eta = None
    for nImage in range(frames):   
        oldTime = time.time() 
        image = Image.new("RGB", (width, height))
        pix = image.load()
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
                    
                # time it took to generate 1 row of pixels   
            if not eta:
                newTime = time.time()
                timeRemaining = (newTime - oldTime) * float(width) * float(frames)
                hours = int(timeRemaining / 3600)
                mins = int(timeRemaining / 60) - hours * 3600
                seconds = int(timeRemaining) - mins * 60
                
                print "Render Time Estimate:",  hours, "hours", mins, "mins", seconds, "seconds"
                eta = True

        myDebug.dprint("Frame " + str(nImage + 1) + " of " + str(frames))
        draw = ImageDraw.Draw(image)
        if (myDebug.enabled()):
            draw.text((0, 0),"Frame: " + str(nImage + 1),(255,255,255))
        draw.text((0, height - 15),"PysiCrystals v" + VERSION,(255,255,255))
        images.append(image)
        layer.update()
    print ("Writing Gif...")
    # duration parameter seems a bit off...
    writeGif(outputFile, images, duration / 20, 0, 0, 0)


