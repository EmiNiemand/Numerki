import matplotlib.pyplot as mplot
import numpy as np
import funkcje_nieliniowe as fn


def draw_function(lower_range, upper_range, function, x0):
    axes = mplot.figure().subplots()
    x = np.linspace(lower_range, upper_range, 100)
    y = function(x)
    axes.scatter(x, y, s=2)
    axes.plot(x, y, "r")
    axes.plot(x0, 0, "b")

    axes.set_xlabel('X')
    axes.set_ylabel('Y')

    mplot.show()
