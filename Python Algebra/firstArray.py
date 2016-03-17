# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 11:33:27 2016

A simple array example with numpy

@author: Tim Metzler
"""

import numpy

# Create array of zeros
z = numpy.zeros(10)
z[4] = 1
print (z)

"""
Other way to do it:
import numpy as np

z = np.zeros(10)
print (z)
"""