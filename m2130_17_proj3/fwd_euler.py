#!/usr/bin/env python
####
# Implementation of the forward Euler method
#
####


def disc_domain(x0, h, N):
    return [x0+ii*h for ii in range(0, N)]

def fwd_euler(f, x0, y0, h, N):
    xs = disc_domain(x0, h, N) 
    ys = [y0]
    for x in xs[1:]:
        ys.append(ys[xs.index(x)-1] + )
