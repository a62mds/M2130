#!/usr/bin/env python
import numpy as np

def vandermonde(xs, degree):
    col = np.array([1]*len(xs))
    mat = np.array(col)
    for d in range(1, degree+1):
        col = np.multiply(col, xs)
        mat = np.r_[mat, col]
    return np.matrix(mat)


if __name__ == '__main__':
    print(vandermonde(np.array([1, 2, 3]), 2))
