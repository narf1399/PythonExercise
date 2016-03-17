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

# Generate a matrix of ones in 3x3 form
print "\n Here is a 3x3 matrix consisting of ones"
myMatrix = numpy.ones(9).reshape(3,3)
print myMatrix, "\n"

# Generate a matrix with random values [3,10) of size 3x2
min = 3
max = 10
myMatrix = numpy.random.random(6).reshape(3,2) * (max - min) + min
print "Here is a matrix with random elements in range of [3,10):"
print myMatrix
print "\n"

# Matrix multiplicate
matrixA = numpy.random.random(6).reshape(3,2) * (max - min) + min
matrixB = numpy.random.random(8).reshape(2,4) * (max - min) + min
print "Multiply matrix A with matrix B"
print "Matrix A:\n", matrixA, "\n"
print "Matrix B:\n", matrixB, "\n"
print "A*B:\n", numpy.dot(matrixA, matrixB)

print "Shape of matrix A:", matrixA.shape
print "Number of rows:", matrixA.shape[0]

# Generate a vector, first element = 0, last element = 2
# no of elements = 20
myVector = numpy.linspace(0,2,20,endpoint=True)[1:]
print "\nA vector starting from 0, ending at 2 with 20 elements:"
print myVector

# Stack matrices, dimensions have to match
print "\nStacking matrices:"
A = numpy.matrix([[2,3,4],[3,5,6],[6,7,8]])
B = numpy.matrix([[5,6,8],[3,5,46],[16,7,8]])
print "A =\n", A
print "B =\n", B
C = numpy.vstack((A,B))
print "C =\n", C
D = numpy.hstack((A,B))
print "D =\n", D

