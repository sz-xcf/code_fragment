import numpy as np


def get_lower_mask(np_arr, threshold):
    mask = np_arr < threshold
    return mask
    # higher_mask = (1-mask).astype(np.bool)
    # then you can use np_arr[mask] = a
