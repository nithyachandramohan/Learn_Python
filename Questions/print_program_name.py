#!/usr/bin/env python3

# Write a program to print name of itself(program name)
import os
import sys

print(os.path.basename(sys.argv[0]))
