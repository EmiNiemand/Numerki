def bisection(fun, lower_range, upper_range, epsilon):
    lower = lower_range
    upper = upper_range
    middle = 0

    accuracy = 0.00001

    for _ in iter(int, 1):
        middle = (lower + upper) / 2
        if abs(lower - upper) > epsilon:
            return middle
        if abs(fun(middle)) < accuracy:
            return middle
        if fun(lower) * fun(middle) > 0:
            lower = middle
        else:
            upper = middle
    return middle


