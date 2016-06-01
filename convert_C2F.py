#!/usr/bin/env python

import sys

def celcius_to_fahr(temp_c):
	temp_f=temp_c* (9.0/5.0) +32
	return temp_f
try:
	cels=float(argv[1])
	print(celcius_to_fahr(cells))

except:
	print("First argument must be a number! Try again)
	
