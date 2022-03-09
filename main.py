# Falsi i bisekcji

import funkcje_nieliniowe as fn
import menu as men
import draw_diagram as dd


def main():
    options = []
    # criterion, acc_formula, function, lower_range, upper_range, epsilon_or_iterations
    # options = men.start()
    # print(options)
    dd.draw_function(-3, 3, fn.trigonometric, 0)

if __name__ == '__main__':
    main()
