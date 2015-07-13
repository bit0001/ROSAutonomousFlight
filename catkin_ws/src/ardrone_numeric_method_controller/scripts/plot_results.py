#!/usr/bin/python3
"""
This is a script for plotting the results after following a trajectory.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2 * math.pi, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()
