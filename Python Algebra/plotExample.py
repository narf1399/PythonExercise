# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 13:14:35 2016

Plotting of a function

@author: Tim Metzler
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 7, 0.1)
y = np.sin(x)
plt.plot(x, y)
