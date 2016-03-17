# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 11:33:27 2016

Some examples of how to use numpy

@author: Tim Metzler
"""
# Or import numpy as np and then use np.zeros(10)
import numpy

# Create array of zeros
z = numpy.zeros(10)
z[4] = 1
print (z)

# A numpy array is not a list
print type(z)

# Create a 2D array
array2D = numpy.array([[1,2],[3,4]])
print array2D

# Get element (1,1)
print array2D[1][1]

# Create a matrix
matrix = numpy.matrix([[1,2],[3,4]])
print matrix
print "The type of the matrix is:", type(matrix)

# Get element (0,1)
print "There are two ways to access a matrix"
print "Get the second element:", matrix.item(1)
print "Get element (0,1):", matrix.item(0,1)

# Get the size of the matrix
print "The size of the matrix is %d." % matrix.size
print "\n"

# Generate numbers from 10 to 49
numbers = numpy.arange(10, 50)
print numbers

print "\nThe last element is:" , numbers[-1]

# Reverse the numbers
reversed = numbers[::-1]
print "The numbers are reversed\n", reversed

# Generate a matrix in 4x4 form
print "\n Here is a 4x4 matrix"
myMatrix = numpy.zeros(16).reshape(4,4)
print myMatrix



