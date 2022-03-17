import sys
import accuracy as ac

def falsi(function, lower_range, upper_range, criterion, eoi):
    if criterion != 3:
        if criterion == 1:
            acc_formula = ac.acc_A
        else:
            acc_formula = ac.acc_B
    else:
        acc_formula = ac.acc_C

    for now_iteration in range(1, sys.maxsize - 1):
        fl = function(lower_range)
        fu = function(upper_range)
        x0 = lower_range - (fl / (fu - fl)) * (upper_range - lower_range)
        if x0 == 0 or (now_iteration > 1 and acc_formula(x0, previous_x0, function, eoi, now_iteration) is True):
            return x0
        elif function(x0) * fl < 0:
            upper_range = x0
        elif function(x0) * fu < 0:
            lower_range = x0
        previous_x0 = x0