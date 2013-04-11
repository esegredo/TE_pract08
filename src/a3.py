#! /usr/bin/python

import random
import sys

# Constant definitions
A = -100
B = 100
numberTests = 1000

# Function definitions
def ab3(a, b):
	return (((a * b) ** 3) == (a**3 * b**3))

def abDiv(a, b):
	return ((a / b) == (1 / (b / a)))

# Main program
if (__name__ == '__main__'):
	if (len(sys.argv) > 1):
		numberTests = int(sys.argv[1])

	fails = 0
	for i in range(numberTests):
		a = random.uniform(A, B)
		b = random.uniform(A, B)
		if (not(ab3(a, b))):
			fails += 1

	print 
	print "Identidad (a*b)^3 = a^3*b^3"
	print "Numero de tests:", numberTests
	print "Porcentaje de fallos:", (100 * fails / float(numberTests)),"%"
	
	fails = 0
	for i in range(numberTests):
		a = random.uniform(A, B)
		b = random.uniform(A, B)
		if (not(abDiv(a, b))):
			fails += 1

	print 
	print "Identidad (a / b) = 1 / (b / a)"
	print "Numero de tests:", numberTests
	print "Porcentaje de fallos:", (100 * fails / float(numberTests)),"%"
