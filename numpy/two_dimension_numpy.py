import numpy as np

# (i) Basics and array creation

# -consists of arrays iinside an array
# -these arrays are of the same size
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# A = np.array(a)
# print(f'A: {A}')
# print(f'Dimension: {A.ndim}')
# No of dimensions is called the rank of that array unlike the matrix
# Rank represents the number of nested lists
# print(f'Shape: {A.shape}')
# A.shape returns a tuple: 1st value represents the number of nested arrays in the array and 2nd value represents the size of each array
# print(f'Size: {A.size}')

X = np.array([[2, 2], [2, 1]])
Y = np.array([[2, 1], [1, 2]])
# Z = X + Y
# print(f'Z: {Z}')

# Z = 2*X
# print(f'Z: {Z}')

# Z = X*Y
# print(f'Z: {Z}')

# Matrix multiplication
A = np.array([[0, 1, 1], [1, 0, 1]])
B = np.array([[1, 1], [1, 1], [-1, 1]])
C = np.dot(A, B)
print(f'C: {C}')

# (ii) Indexing and slicing
# print(f'A[1][2]: {A[1][2]}')
# print(f'A[0, 0:2]: {A[0, 0:2]}')
# print(f'A[0:2, 0:2]: {A[0:2, 0:2]}')

# (iii) Basic operations