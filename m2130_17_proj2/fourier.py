#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

PI = np.pi

xs = np.linspace(-PI, PI, 1001)

f = lambda x: x*x*x

def plot(func, domain):
    plt.plot(domain, map(func, domain))
    plt.show()

