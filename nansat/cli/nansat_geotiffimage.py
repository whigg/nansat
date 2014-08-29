#!/usr/bin/env python
#
# Utility to make an 8-bit Geotiff figure for one band of a Nansat dataset
# Scaling ("minmax") and colormap from VKW is applied

import sys

from nansat import Nansat

tmpVRTfileName = 'tmp.VRT'

def Usage():
    sys.exit('Usage: nansat_geotiffimage <band> <input_file> <output_file>')

def main():
    if (len(sys.argv) <= 2):
        Usage()
    
    try:
        bandNo = int(sys.argv[1])
        infileName = sys.argv[2]
        outfileName = sys.argv[3]
    except:
        Usage()
    
    n = Nansat(infileName)
    n.write_geotiffimage(outfileName, bandNo)
    
if __name__ == '__main__':
    main()