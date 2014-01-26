#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
from layer import Layer

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_const',
                        const=True, help='enable verbose output')
    parser.add_argument('config_file', help='configuration file to load')
    parser.add_argument('output_file', help='output filename')
    args = vars(parser.parse_args())
    v = args['verbose']
    
    if v:
        print "VERBOSE!"


