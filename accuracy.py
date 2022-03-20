def acc_A(lower, upper, fun, epsilon, now_iteration):
    return abs(upper - lower) < epsilon


def acc_B(lower, upper, fun, epsilon, now_iteration):
    return abs(fun(upper)) < epsilon


def acc_C(lower, upper, fun, iteration, now_iteration):
    return iteration <= now_iteration
