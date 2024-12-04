import numpy as np

input_text = open("input.txt").read()

matrix = np.array([[c for c in row] for row in input_text.split("\n")])
kernel = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]])

def sliding_window(matrix, kernel_dim):
        # How many strides can we fit in the matrix
        shape = tuple(dn - wn + 1 for dn, wn in zip(matrix.shape, kernel_dim)) + kernel_dim
        # How many bytes to skip to get to the next window
        strides = matrix.strides * 2

        return np.lib.stride_tricks.as_strided(matrix, shape=shape, strides=strides)

def arrays_from_kernel(matrix, kernel):
        windows = sliding_window(matrix, kernel.shape)
        return np.where(kernel, windows, '')

sub_arrays = arrays_from_kernel(matrix, kernel).reshape(-1, 3, 3)
words = ["MSAMS", "MMASS", "SMASM", "SSAMM"]
text = ' '.join([''.join(x.flatten()) for x in sub_arrays])
count = sum([text.count(word) for word in words])

print(count)
