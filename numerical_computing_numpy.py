# NumPy provides a multidimensional array object
# to store homogeneous or heterogeneous data arrays
# and supports vectorization of code

# ndarray (regular)
# n-dimensional array object
# used for large arrays of numerical data

# ndarray (record)
# 2-dimensional array object
# Tabular data organized in columns

# vectorization is a strategy to get more
# compact code that executes faster

# the concept is to apply a function or
# operation on a complex object at once
# rather than looping over it 

# numpy allows broadcasting, which is
# the combination of data of different shapes

import numpy as np 

np.random.seed(100)

r = np.arrange(12).reshape((4, 3))

# broadcasting
r + 3

2 * r