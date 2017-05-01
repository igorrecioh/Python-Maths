#!/usr/bin/env python

import math, time
from CoordenatesConversion import *

print "1 - Cartesianas a cilindricas"
print "2 - Cartesianas a esfericas"
print "3 - Cartesianas a polares"
print "4 - Cilindricas a cartesianas"
print "5 - Esfericas a cartesianas"
print "6 - Polares a cartesianas"

key=int(raw_input("Conversion de coordenadas a realizar: "))

if key == 1:
	CartACil()
if key == 2:
	CartAEsf()
if key == 3:
	CartAPolar()
if key == 4:
	CilACart()
if key == 5:
	EsfACart()
if key == 6:
	PolarACart()