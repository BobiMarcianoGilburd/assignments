#!/usr/bin/env python2

# Calculator.py
# This program defines four functions: multiply, add, subtract, and divide.
# Each functions takes two arguments and return the operator's arithmetric result
# (no output is printed to the screen).

# multiply - this function multiplies two numbers and returns the result.
# Input  : a, b
# Returns: a * b
def multiply(a, b):
	return a * b

# add - this function adds two numbers and returns the result.
# Input  : a, b
# Returns: a + b
def add(a, b):
	return a + b

# subtract - this function substracts two numbers and returns the result.
# Input  : a, b
# Returns: a - b
def subtract(a, b):
	return a - b

# divide - this function divides two numbers and returns the result.
# Input  : a, b
# Returns: a / b
def divide(a, b):
	return a / b

# The program will start running from here
# Call the multiply function defined above
print "I'm going use the calculator functions to multiply 5 and 6"
x = multiply(5,6)
print x

