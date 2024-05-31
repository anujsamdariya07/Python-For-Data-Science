import numpy as np
import matplotlib.pyplot as plt

# (i) Basics and array creation

# -Fixed in size
# -Contains elements of same data type
# a = np.array([0, 1, 2, 3, 4])
# print(a)
# print(type(a))
# print(a.dtype)
# print(a.size)
# print(a.ndim) # no of dimensions
# print(a.shape)

# b = np.array([0.1, 1.1, 2.1, 3.1, 4.1])
# print(type(b))
# print(b.dtype)

# (ii) Indexing and slicing
# c = np.array([20, 1, 2, 3, 4])
# print(f'c: {c}')
# c[0] = 100
# print(f'c: {c}')
# c[4] = 0
# print(f'c: {c}')

# d = c[1:4]
# print(f'd: {d}')

# c[3:5] = 400, 500
# print(f'c: {c}')

# (iii) Basic operations

# Vector addition
# u = [1, 0]
# v = [0, 1]
# w = []
# for n, m in zip(u, v):
#   w.append(n+m)
# print(f'w: {w}')

# x = np.array([1, 0])
# y = np.array([0, 1])
# z = x+y
# print(f'z: {z}')

# a = np.array([1, 0])
# b = np.array([0, 1])
# c = x-y
# print(f'c: {c}')

# Array mutiplication with a scalar
# p = np.array([1, 2])
# q = 2*p
# print(f'q: {q}')

# Product of 2 numpy arrays
# u = np.array([1, 2])
# v = np.array([3, 2])
# w = u*v
# print(f'w: {w}')

# Dot Product
# u = np.array([1, 2])
# v = np.array([3, 1])
# dot_product = np.dot(u, v)
# print(f'Dot Product: {dot_product}')

# Adding constant to a numpy array
# u = np.array([1, 2, 3, -1])
# z = u + 1
# print(f'z: {z}')

# (iv) Universal functions

# Mean of an array
# a = np.array([1, -1, 1, -1])
# mean_a = a.mean()
# print(f'Mean of a: {mean_a}')

# Maximum of an array
# b = np.array([1, -2, 3, 4, 5])
# max_b = b.max()
# print(f'Max of b: {max_b}')

# Sine in an array
# x = np.array([0, (np.pi)/2, np.pi])
# y = np.sin(x)
# print(f'y: {y}')

# For plotting mathematical functions
# m = np.linspace(-2, 2, num=5)
# print(f'm: {m}')

# m = np.linspace(-2, 2, num=9)
# print(f'm: {m}')

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
# %matplotlib inline
# print(plt.plot(x, y)) --> on jupyter notebook