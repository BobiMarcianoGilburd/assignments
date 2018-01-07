#!/usr/bin/env python

# This Python scripts Reads a string from STDIN and print
# it to STDOUT after adding the string "Hello " at the beginning
# and "!" at the end.

import sys
name = sys.stdin.read()
print "Hello " + name + "!"
