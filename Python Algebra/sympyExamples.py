# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 12:42:24 2016

Some of this only seems to work in the console

@author: Tim Metzler
"""

from sympy import *
# from sympy import symbols

# Define variables as symbols (so we can change the value of those later)
x = symbols('x')
y = symbols('y')

# Differentation
print diff(cos(x), x)

# Integration

print integrate(ln(x), x)
expr = integrate(exp(exp(x)),x)
init_printing()
print expr

# Solve equations
print simplify(Eq(x+1, 4))

# Simple equations
myEquation = Eq(x + 1, 4)
print myEquation

# Differential equations
f, g = symbols('f g', cls=Function)
diffeq = Eq(f(x).diff(x, x) - 2*f(x).diff(x) + f(x), sin(x))

print diffeq

# Solve
print dsolve(diffeq, f(x))










