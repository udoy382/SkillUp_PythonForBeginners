# Numpy Library in Python

import numpy as np
import time
import sys

a = np.array([1, 2, 3])
# print(a)
# print(a[0])

b = range(1000)
# print(sys.getsizeof(5)* len(b))

c = np.arange(1000)
# print(c.size*c.itemsize)


size = 10000

l1 = range(size)
l2 = range(size)
A1 = np.arange(size)
A2 = np.arange(size)


start = time.time()
result = [(x+y) for x, y in zip(l1, l2)]
# print(result)

rst = A1 + A2
# print(rst)


z = np.array([[1, 2], [1, 4], [1, 6]])
# print(z)
# print(z.ndim)
# print(z.itemsize)
# print(a.shape)


z2 = np.array([[1, 2], [1, 4], [1, 6]], dtype=np.float64)
# print(z2)
# print(z2.itemsize)
# print(z2.shape)


# print(np.zeros((3, 4)))
# print(np.ones((3, 4)))


# print(np.char.capitalize("hello World"))
# print(np.char.lower("Hello World"))
# print(np.char.upper("Hello World"))
# print(np.char.title("Hello World"))
# print(np.char.split("Hello World"))
# print(np.char.splitlines("Hello World\nhow are you"))
# print(np.char.strip(["hey", "there", "how", "are", "you"], "k"))
# print(np.char.join([":" "," "-"], ["hey", "there"]))
print(np.char.replace("He is a good dancer", "is", "was"))