#!/usr/bin/env python
# testing Pythonic version of am2130 project solns
from math import cos


sq = lambda x: x*x

f = lambda x: cos(sq(x))

def fact(n):
    return 1 if n == 1 else n*fact(n-1)

def a(m):
    return 1.0/fact(2.0*(m-1))/(4.0*m-1)*(1.0/2.0)**(4.0*(m-1))


