#!/usr/bin/env python

import math, time

def CartACil():
	print " "
	print "* - Conversor de coordenadas cartesianas a cilindricas (3D) - *"
	print "---------------------------------------------------------------"
	time.sleep(1)

	try:
	    x=float(raw_input('Coordenada X: '))
	except ValueError:
	    print "No es numero real"

	try:
 	   y=float(raw_input('Coordenada Y: '))
 	except ValueError:
	   print "No es numero real"

	try:
 	   z=float(raw_input('Coordenada Z: '))
	except ValueError:
	    print "No es numero real"

	rho = math.sqrt((x**2)+(y**2))	
	phi = math.atan2(y,x)
	z1 = z

	print "	Coordenadas cilindricas: "	
	print "		rho = "+ "%.3f" %(rho)
	print "		phi = "+ "%.3f" %(phi)
	print "		z = "+ "%.3f" %(z1)
	print "		(%.3f,%.3f,%.3f)" %(rho,phi,z1)
	print ""


def CartAEsf():
	print " "
	print "* - Conversor de coordenadas cartesianas a esfericas (3D) - *"
	print "-------------------------------------------------------------"
	time.sleep(1)

	try:
  	  x=float(raw_input('Coordenada X: '))
	except ValueError:
  	  print "No es numero real"

	try:
 	   y=float(raw_input('Coordenada Y: '))
	except ValueError:
  	  print "No es numero real"

	try:
  	  z=float(raw_input('Coordenada Z: '))
	except ValueError:
  	  print "No es numero real"

	r = math.sqrt((x**2)+(y**2)+(z**2))
	aux = math.sqrt((x**2)+(y**2))
	theta = math.atan2(aux,z)
	phi = math.atan2(y,x)

	print "	Coordenadas esfericas: "
	print "		r = "+ "%.3f" %(r)
	print "		theta = "+ "%.3f" %(theta)
	print "		phi = "+ "%.3f" %(phi)
	print "		(%.3f,%.3f,%.3f)" %(r,theta,phi)
	print ""

def CartAPolar():
	print " "
	print "* - Conversor de coordenadas cartesianas a polares (2D) - *"
	print "-----------------------------------------------------------"
	time.sleep(1)

	try:
	    x=float(raw_input('Coordenada X: '))
	except ValueError:
	    print "No es numero real"

	try:
	    y=float(raw_input('Coordenada Y: '))
	except ValueError:
	    print "No es numero real"

	r = math.sqrt((x**2)+(y**2))
	t0 = math.atan2(y,x)
	t1 = math.degrees(t0)

	print "	Coordenadas polares: "
	print "		r = "+ "%.3f" %(r)
	print "		theta = "+ "%.3f" %(t1)
	print "		(%.3f,%.3f)" %(r,t1)
	print ""

def CilACart():
	print " "
	print "* - Conversor de coordenadas cilindricas a cartesianas (3D) - *"
	print "---------------------------------------------------------------"
	time.sleep(1)

	try:
   		rho=float(raw_input('Rho: '))
	except ValueError:
	    print "No es numero real"

	try:
	    phi=float(raw_input('Phi: '))
	except ValueError:
	    print "No es numero real"

	try:
	    z1=float(raw_input('Z: '))
	except ValueError:
	    print "No es numero real"

	x = rho * math.cos(phi)
	y = rho * math.sin(phi)
	z = z1

	print "	Coordenadas cartesianas: "
	print "		x = "+ "%.3f" %(x)
	print "		y = "+ "%.3f" %(y)
	print "		z = "+ "%.3f" %(z)
	print "		(%.3f,%.3f,%.3f)" %(x,y,z)
	print ""

def EsfACart():
	print " "
	print "* - Conversor de coordenadas esfericas a cartesianas (3D) - *"
	print "-------------------------------------------------------------"
	time.sleep(1)

	try:
		r=float(raw_input('R: '))
	except ValueError:
		print "No es numero real"

	try:
		theta=float(raw_input('Theta: '))
	except ValueError:
		print "No es numero real"

	try:
		phi=float(raw_input('Phi: '))
	except ValueError:
		print "No es numero real"

	x = r * math.sin(theta) * math.cos(phi)
	y = r * math.sin(theta) * math.sin(phi)
	z = r * math.cos(theta)

	print "	Coordenadas cartesianas: "
	print "		x = "+ "%.3f" %(x)
	print "		y = "+ "%.3f" %(y)
	print "		z = "+ "%.3f" %(z)
	print "		(%.3f,%.3f,%.3f)" %(x,y,z)
	print ""

def PolarACart():
	print " "
	print "* - Conversor de coordenadas polares a cartesianas (2D) - *"
	print "-----------------------------------------------------------"
	time.sleep(1)

	try:
	    r=float(raw_input('Modulo (r): '))
	except ValueError:
 	   print "No es numero real"

	try:
 	   t=float(raw_input('Angulo: '))
	except ValueError:
 	   print "No es numero real"

	x = r * math.cos(math.radians(t))
	y = r * math.sin(math.radians(t))

	print "	Coordenadas cartesianas: "
	print "		x = "+ "%.3f" %(x)
	print "		y = "+ "%.3f" %(y)
	print "		(%.3f,%.3f)" %(x,y)
	print ""