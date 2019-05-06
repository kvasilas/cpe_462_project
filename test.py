import numpy as np

def clip_array(arr):
    max_val = 6
    min_val = 3
    comp_arr = np.ones_like(arr)
    arr = np.maximum(comp_arr * min_val, arr)
    arr = np.minimum(comp_arr * max_val, arr)
    return arr

a = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 8]
print(np.clip(a, 3, 6))
print(clip_array(a))
