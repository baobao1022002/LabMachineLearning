import numpy as np


def __replace_greater_than__(arr, val):
    arr[arr > val] = val
    return arr

# Example usage
arr = np.array([[0.42, 0.48, 0.32],
                [0.74, 0.58, 0.38],
                [0.51, 0.34, 0.15]])
val = 0.5
new_arr = __replace_greater_than__(arr, val)
print(new_arr)


