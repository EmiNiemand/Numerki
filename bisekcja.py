import sys


def bisection(fun, lower_range, upper_range, epsilon_or_iteration, criterion):
    lower = lower_range
    upper = upper_range

    if criterion != 3:
        if criterion == 1:
            acc_formula = bisection_A
        else:
            acc_formula = bisection_B
    else:
        acc_formula = bisection_C

    for now_iteration in range(1, sys.maxsize - 1):
        middle = (lower + upper) / 2
        if acc_formula(lower, upper, fun, epsilon_or_iteration, now_iteration):
            return middle
        if fun(lower) * fun(middle) > 0:
            lower = middle
        else:
            upper = middle


def bisection_A(lower, upper, fun, epsilon, now_iteration):
    return abs(upper - lower) < epsilon


def bisection_B(lower, upper, fun, epsilon, now_iteration):
    return abs(fun(upper)) < epsilon


def bisection_C(lower, upper, fun, iteration, now_iteration):
    return iteration <= now_iteration
