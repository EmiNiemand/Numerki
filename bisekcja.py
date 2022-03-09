def bisection(fun, acc_formula, lower_range, upper_range, epsilon):
    lower = lower_range
    upper = upper_range
    middle = (lower + upper) / 2

    for _ in iter(int, 1):
        if acc_formula(lower, upper, acc_formula) > epsilon:
            return middle
        if fun(lower) * fun(middle) > 0:
            lower = middle
        else:
            upper = middle
        middle = (lower + upper) / 2


def bisection_A(lower, upper, fun):
    return abs(upper - lower)


def bisection_B(lower, upper, fun):
    return abs(fun(upper))

