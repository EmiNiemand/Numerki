# Falsi i bisekcji

import menu as men
import draw_diagram as dd
import falsi as fs
import bisekcja as bi
import funkcje_nieliniowe as fn


def main():
    # options contain:
    # criterion, function, lower_range, upper_range, epsilon_or_iterations
    options = men.start()
    dd.draw_function(options[2], options[3], options[1],
                     fs.falsi(options[1], options[2], options[3], options[0], options[4]))
    dd.draw_function(options[2], options[3], options[1],
                     bi.bisection(options[1], options[2], options[3], options[0], options[4]))


if __name__ == '__main__':
    main()
