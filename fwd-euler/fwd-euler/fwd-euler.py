#!/usr/bin/env python
# fwd-euler/fwd-euler.py

from matplotlib import pyplot as plt


def fwd_euler(f, x, y, h, n):
    xs = [x]
    ys = [y]
    for ii in range(0, n):
        y = y + h*f(x, y)
        x = x + h
        ys.append(y)
        xs.append(x)
    return (xs, ys)

def imp_fwd_euler(f, x, y, h, n):
    xs = [x]
    ys = [y]
    for ii in range(0, n):
        k = h*f(x, y)
        l = h*f(x+h, y+k)
        y = y + 0.5*(k + l)
        x = x + h
        ys.append(y)
        xs.append(x)
    return (xs, ys)


def main():
    f = lambda x, y: 1.0/(1.0 + x*x) - 2.0*y*y
    h = 0.2
    n = 10
    x0 = 0
    y0 = 0
    plt.plot(*fwd_euler(f, x0, y0, h, n), linestyle='--', color='blue')
    plt.plot(*imp_fwd_euler(f, x0, y0, h, n), linestyle='--', color='red')
    plt.show()


if __name__=='__main__':
    main()


#EOF
