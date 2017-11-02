#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 08:48 2017

@author: simon
"""

# Import libraries
import os

# Get working directory
wdir = os.getcwd()


# Loop over files in directory
for root, dirs, filenames in os.walk(wdir):
    for f in filenames:
        # Open file
        h = open(f,"rb")
        
        # Read lines
        lines = h.readlines()
        
        # Close read and reopen for write
        h.close()
        
        # Delete file
        os.remove(f)
        
        h = open(f,"wb")
        
        # Dont write inciminating line
        for line in lines:
          if line != b'CA[HANGEUL_CHARSET]\n': h.write(line)
          
        # Close file
        h.close()

