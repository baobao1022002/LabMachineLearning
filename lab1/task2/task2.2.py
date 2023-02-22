import numpy as np

# Input array
arr = np.array([1, 2, 3, 4])
print("Original array:", arr)

# Repeating 2 times
arr_2 = np.tile(arr, 2)
print("Repeating 2 times:", arr_2)

# Repeating 3 times
arr_3 = np.tile(arr, 3)
print("Repeating 3 times:", arr_3)