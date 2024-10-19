# Matplotlib in Python


import matplotlib
import numpy as np
import pylab

# Use numpy to generate3 random data ~
"""
x = np.linspace(0, 10, 25)
y = x * x + 2
print(x)
print(y)
print(np.array([x, y]).reshape(25, 2).reshape(2, 25))
"""

# It only takes 1 command to draw ~
"""
x = np.linspace(0, 10, 25)
y = x * x + 2
# print(pylab.plot(x, y, 'r')) # stands for red
pylab.subplot(1, 2, 1)
pylab.plot(x,y, 'r--')

pylab.subplot(1,2, 2)
pylab.plot(y, x, 'g-')
pylab.show()
"""

# This code I copy form google for practice ~
"""
x = np.linspace(-3, 3, 30)
y = x**2
pylab.plot(x, y)
pylab.show()
"""
"""
x = np.linspace(-3, 3, 30)
y = x**2
pylab.plot(x, pylab.sin(x))
pylab.plot(x, pylab.cos(x), 'r-')
pylab.plot(x, pylab.sin(x), 'g--')
pylab.show()
"""
