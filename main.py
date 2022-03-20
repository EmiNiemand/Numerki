# Falsi i bisekcji

import menu as men
import draw_diagram as dd
import falsi as fs
import bisekcja as bi
import funkcje_nieliniowe as fn


def main():
    # options contain:
    # criterion, function, lower_range, upper_range, epsilon_or_iterations
    # options = men.start()
    # print(options)
    # dd.draw_function(options[2], options[3], options[1],
    #                  fs.falsi(options[1], options[2], options[3], options[0], options[4]))
    # dd.draw_function(options[2], options[3], options[1],
    #                  bi.bisection(options[1], options[2], options[3], options[0], options[4]))
    #
#==========================================================================================
    dd.draw_function(-1, 1.5, fn.polynomial, bi.bisection(fn.polynomial, -1, 1.5, 1, 0.001))
    dd.draw_function(-1, 1.5, fn.polynomial, bi.bisection(fn.polynomial, -1, 1.5, 2, 0.001))
    dd.draw_function(-1, 1.5, fn.polynomial, bi.bisection(fn.polynomial, -1, 1.5, 3, 5))

    dd.draw_function(-3, 2, fn.trigonometric, bi.bisection(fn.trigonometric, -3, 2, 1, 0.001))
    dd.draw_function(-3, 2, fn.trigonometric, bi.bisection(fn.trigonometric, -3, 2, 2, 0.001))
    dd.draw_function(-3, 2, fn.trigonometric, bi.bisection(fn.trigonometric, -3, 2, 3, 5))

    dd.draw_function(-0.5, 2, fn.exponential, bi.bisection(fn.exponential, -0.5, 2, 1, 0.001))
    dd.draw_function(-0.5, 2, fn.exponential, bi.bisection(fn.exponential, -0.5, 2, 2, 0.001))
    dd.draw_function(-0.5, 2, fn.exponential, bi.bisection(fn.exponential, -0.5, 2, 3, 5))

    dd.draw_function(-0.33, 1.2, fn.polynomial_trigonometric,
                     bi.bisection(fn.polynomial_trigonometric, -0.33, 1.2, 1, 0.001))
    dd.draw_function(-0.33, 1.2, fn.polynomial_trigonometric,
                     bi.bisection(fn.polynomial_trigonometric, -0.33, 1.2, 2, 0.001))
    dd.draw_function(-0.33, 1.2, fn.polynomial_trigonometric, bi.bisection(fn.polynomial_trigonometric, -0.33, 1.2, 3, 5))

    dd.draw_function(-3, 5.7, fn.trigonometric_exponential, bi.bisection(fn.trigonometric_exponential, -3, 5.7, 1, 0.001))
    dd.draw_function(-3, 5.7, fn.trigonometric_exponential, bi.bisection(fn.trigonometric_exponential, -3, 5.7, 2, 0.001))
    dd.draw_function(-3, 5.7, fn.trigonometric_exponential, bi.bisection(fn.trigonometric_exponential, -3, 5.7, 3, 5))

    dd.draw_function(-0.1, 1, fn.polynomial_exponential, bi.bisection(fn.polynomial_exponential, -0.1, 1, 1, 0.001))
    dd.draw_function(-0.1, 1, fn.polynomial_exponential, bi.bisection(fn.polynomial_exponential, -0.1, 1, 2, 0.001))
    dd.draw_function(-0.1, 1, fn.polynomial_exponential, bi.bisection(fn.polynomial_exponential, -0.1, 1, 3, 5))



#==========================================================================================
    dd.draw_function(-1, 1.5, fn.polynomial, fs.falsi(fn.polynomial, -1, 1.5, 1, 0.001))
    dd.draw_function(-1, 1.5, fn.polynomial, fs.falsi(fn.polynomial, -1, 1.5, 2, 0.001))
    dd.draw_function(-1, 1.5, fn.polynomial, fs.falsi(fn.polynomial, -1, 1.5, 3, 5))

    dd.draw_function(-3, 2, fn.trigonometric, fs.falsi(fn.trigonometric, -3, 2, 1, 0.001))
    dd.draw_function(-3, 2, fn.trigonometric, fs.falsi(fn.trigonometric, -3, 2, 2, 0.001))
    dd.draw_function(-3, 2, fn.trigonometric, fs.falsi(fn.trigonometric, -3, 2, 3, 5))

    dd.draw_function(-0.5, 2, fn.exponential, fs.falsi(fn.exponential, -0.5, 2, 1, 0.001))
    dd.draw_function(-0.5, 2, fn.exponential, fs.falsi(fn.exponential, -0.5, 2, 2, 0.001))
    dd.draw_function(-0.5, 2, fn.exponential, fs.falsi(fn.exponential, -0.5, 2, 3, 5))

    dd.draw_function(-0.33, 1.2, fn.polynomial_trigonometric, fs.falsi(fn.polynomial_trigonometric, -0.33, 1.2, 1, 0.001))
    dd.draw_function(-0.33, 1.2, fn.polynomial_trigonometric, fs.falsi(fn.polynomial_trigonometric, -0.33, 1.2, 2, 0.001))
    dd.draw_function(-0.33, 1.2, fn.polynomial_trigonometric, fs.falsi(fn.polynomial_trigonometric, -0.33, 1.2, 3, 5))

    dd.draw_function(-3, 5.7, fn.trigonometric_exponential, fs.falsi(fn.trigonometric_exponential, -3, 5.7, 1, 0.001))
    dd.draw_function(-3, 5.7, fn.trigonometric_exponential, fs.falsi(fn.trigonometric_exponential, -3, 5.7, 2, 0.001))
    dd.draw_function(-3, 5.7, fn.trigonometric_exponential, fs.falsi(fn.trigonometric_exponential, -3, 5.7, 3, 5))

    dd.draw_function(-0.1, 1, fn.polynomial_exponential, fs.falsi(fn.polynomial_exponential, -0.1, 1, 1, 0.001))
    dd.draw_function(-0.1, 1, fn.polynomial_exponential, fs.falsi(fn.polynomial_exponential, -0.1, 1, 2, 0.001))
    dd.draw_function(-0.1, 1, fn.polynomial_exponential, fs.falsi(fn.polynomial_exponential, -0.1, 1, 3, 5))


if __name__ == '__main__':
    main()
