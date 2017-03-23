#!/usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt

from vandermonde import vandermonde

dens = np.array([2.8, 2.9, 3.0, 3.1, 3.2, 3.2, 3.2, 3.3, 3.4])    # grams/cm^3
iron = np.array([ 30,  26,  33,  31,  33,  35,  37,  36,  33])    # percent content

if len(dens) == len(iron):
    data = np.array([(dens[ii], iron[ii]) for ii in range(len(dens))])
else:
    raise ValueError('Arrays must be of same length')

