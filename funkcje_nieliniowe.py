import math


def polynomial(x):
    return ((2 * x + 2) * x + 4) * x - 1


def trigonometric(x):
    return math.sin(x)


def exponential(x):
    return 2 ** x - 2


def polynomial_trigonometric(x):
    return ((2 * x + 2) * x + 4) * x + math.sin(x)


def trigonometric_exponential(x):
    return math.sin(x) + 2 ** x - 2


def polynomial_exponential(x):
    return ((2 * x + 2) * x + 4) * x - 2 ** x - 2
