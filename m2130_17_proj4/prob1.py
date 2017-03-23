#!/usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt

dens = np.array([2.8, 2.9, 3.0, 3.1, 3.2, 3.2, 3.2, 3.3, 3.4])    # grams/cm^3
iron = np.array([ 30,  26,  33,  31,  33,  35,  37,  36,  33])    # percent content

if len(dens) == len(iron):
    data = np.array([(dens[ii], iron[ii]) for ii in range(len(dens))])
else:
    raise ValueError('Arrays must be of same length')

def vandermonde(xs, degree):
    mat = np.array(np.array([1]*len(xs)))
    for d in range(1, degree):
        xs = np.multiply(mat[d-1], xs)
        mat = np.r_[mat, xs]
    return np.matrix(mat)

# vandermonde generating a 1-col matrix (should be 2 cols)
print(vandermonde(np.array([2, 2, 2]), 2))
