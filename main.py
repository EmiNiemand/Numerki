# Falsi i bisekcji

import menu as men
import draw_diagram as dd
import falsi as fs
import bisekcja as bi


def main():
    # options contain:
    # criterion, function, lower_range, upper_range, epsilon_or_iterations
    options = men.start()
    print(options)
    dd.draw_function(options[2], options[3], options[1],
                     fs.falsi(options[0], options[1], options[2], options[3], options[4]))
    dd.draw_function(options[2], options[3], options[1],
                     bi.bisection(options[1], options[2], options[3], options[4], options[0]))


if __name__ == '__main__':
    main()
