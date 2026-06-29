import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(arr.shape)
print(type(arr))
print(len(arr))

# Useful Attributes
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(arr.shape) # Dimensions - (4 x 3)
print(arr.size) # Total elements - (12)
print(arr.ndim) # Number of dimensions - 2
print(arr.dtype) # Data type object - int64
print(arr.itemsize) # Size of each element in bytes - 8 for int64

# Broadcasting with a Scalar
arr_mul10 = arr * 10 # Multiply by 10 to all nums
print(arr_mul10)
# Broadcasting with a Vector
arr1D = np.array([1, 2, 3])
arr2D = np.array([[1, 2, 3], [4, 5, 6]])
print(arr1D + arr2D)

arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr)) # 15
print(np.prod(arr)) # 120
print(np.min(arr)) # 1
print(np.argmin(arr)) # 0
print(np.max(arr)) # 5
print(np.argmax(arr)) # 4
print(np.mean(arr)) # 3.0
print(np.median(arr)) # 3.0
print(np.std(arr)) # 1.41
print(np.var(arr)) # 2.0