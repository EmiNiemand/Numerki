import sys
import accuracy as ac

def bisection(fun, lower_range, upper_range, criterion, epsilon_or_iteration):
    lower = lower_range
    upper = upper_range

    if criterion != 3:
        if criterion == 1:
            acc_formula = ac.acc_A
        else:
            acc_formula = ac.acc_B
    else:
        acc_formula = ac.acc_C

    for now_iteration in range(1, sys.maxsize - 1):
        middle = (lower + upper) / 2
        if middle == 0 or acc_formula(lower, upper, fun, epsilon_or_iteration, now_iteration):
            return middle
        if fun(lower) * fun(middle) > 0:
            lower = middle
        else:
            upper = middle