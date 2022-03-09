def falsi(criterion, function, lower_range, upper_range, eoi):
    x0 = 0
    checker = False
    # |x_i−x_(i−1)| < ε
    if criterion == 1:
        for _ in iter(int, 1):
            if checker is True:
                previous_x0 = x0
            fl = function(lower_range)
            fu = function(upper_range)
            x0 = lower_range - (fl / (fu - fl)) * (upper_range - lower_range)
            if x0 == 0:
                return x0
            elif function(x0) * fl < 0:
                upper_range = x0
            elif function(x0) * fu < 0:
                lower_range = x0
            if checker is True and (x0 - previous_x0) < eoi:
                return x0
    # |f(x_i)| < ε
    if criterion == 2:
        for _ in iter(int, 1):
            fl = function(lower_range)
            fu = function(upper_range)
            x0 = lower_range - (fl / (fu - fl)) * (upper_range - lower_range)
            if x0 == 0 or abs(function(x0)) < eoi:
                return x0
            elif function(x0) * fl < 0:
                upper_range = x0
            elif function(x0) * fu < 0:
                lower_range = x0
    # iteration number
    if criterion == 3:
        for i in range(eoi):
            fl = function(lower_range)
            fu = function(upper_range)
            x0 = lower_range - (fl / (fu - fl)) * (upper_range - lower_range)
            if x0 == 0:
                return x0
            elif function(x0) * fl < 0:
                upper_range = x0
            elif function(x0) * fu < 0:
                lower_range = x0
        return x0
