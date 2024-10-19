# Library in Python

import numpy as np
from scipy import constants
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style


# Top 5 Library for Data science ==>
# 1) Tensorflow
# 2) Numpy
# 3) Scipy
# 4) Pandas
# 5) Matplotlib


# Ex. Numpy ==>
"""
a = np.array([1, 2, 3])
print(type(a))

# print(a.shape)

b = np.arange(12)
print(b)

b.reshape(3, 4)
"""


# Ex. Scipy ==>
"""
print(constants.c) # spred of light
print(constants.h) # Plank's constant
print(constants.N_A) # Avogadro's number
"""


# Ex. Pandas ==>
"""
df = pd.DataFrame(np.random.randn(6, 4), index=list(range(6)), columns=list('ABCD'))
print(df)

df.describe()
"""


# Ex. Matplotlib ==>
"""
np.random.seed(10)

N = 30
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)

area = (30 * np.random.random(N))**2

plt.scatter(x, y, s=area, c=colors, alpha=0.4)
# plt.show()
"""

# -------------------->

"""
style.use('ggplot')
a = [2, 4, 6]
b = [2, 14, 16]

a2 = [3, 3, 4]
b2 = [7, 14, 5]

plt.bar(a, b, color='r', align='center')
plt.bar(a2, b2, color='b', align='center')


plt.title("Info")
plt.ylabel("Y axis")
plt.xlabel("X axis")

plt.show()
"""
