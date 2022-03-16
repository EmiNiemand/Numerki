import matplotlib.pyplot as mplot
import numpy as np


def draw_function(lower_range, upper_range, function, x0):
    axes = mplot.figure().subplots()
    x = np.linspace(lower_range, upper_range, 100)
    y = []
    for i in x:
        y.append(function(i))
    axes.plot(x, y, "r")
    axes.plot(x0, function(x0), marker=".", color="b")

    axes.set_xlabel('X')
    axes.set_ylabel('Y')

    mplot.show()