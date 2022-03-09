import math


def start():
    criterion = choose_criterion()
    function = choose_function()
    upper_range, lower_range = choose_range(function)

    if criterion == 1:
        return criterion, function, upper_range, lower_range, float(input("epsilon: "))
    return criterion, function, upper_range, lower_range, float(input("Liczba iteracji: "))


def choose_criterion():
    for _ in iter(int, 1):
        print("Wybierz kryterium zatrzymania: ",
              "\n1=Warunek nałożony na dokładność",
              "\n2=Liczba iteracji")
        a = float(input("wariant: "))

        if a == 1 or a == 2:
            return a
        print("Wybierz prawidłowy wariant (1 lub 2)")


def choose_function():
    for _ in iter(int, 1):
        print("Wybierz funkcję: ",
              "\n1=((2*x+2)*x+4)*x-1",
              "\n2=sin(x)"
              "\n3=2**x-2")
        a = float(input("funkcja: "))

        if a == 1 or a == 2 or a == 3:
            return a
        print("Wybierz prawidłową liczbę (1 lub 2 lub 3)")


def choose_range(function):
    for _ in iter(int, 1):
        print("Wybierz przedział na którym mam szukać miejsca zerowego:")
        lower_range = float(input("dolny przedział: "))
        upper_range = float(input("górny przedział: "))
        if lower_range < 0 < upper_range:
            if function == 2 and abs(lower_range) + upper_range > math.pi:
                continue
            return lower_range, upper_range
        print("Wybierz prawidłowy przedział (dolny przedział < 0 i górny przedział > 0)")


# eval
