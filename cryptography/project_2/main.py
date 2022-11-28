from tasks.calc_sum_points import calc_sum_points
from tasks.get_inverse_point import get_inverse_point
from tasks.get_multiply_point import get_multiply_point
from tasks.get_random_point import get_random_point
from tasks.rand_elliptical_curve import rand_elliptical_curve

if __name__ == '__main__':
    while True:
        description = """
        1. Wygeneruj losową krzywą eliptyczną
        2. Znajdź losowy punkt na krzywej
        3. Oblicz punkt przeciwny
        4. Oblicz PoQ sumę punktow krzywej eliptycznej
        5. Oblicz n-tą krotność punktu P

        q - zamknij program
        """
        print(description)
        command = input('Podaj komendę: ')

        match command:
            case '1':
                rand_elliptical_curve()
            case '2':
                get_random_point()
            case '3':
                get_inverse_point()
            case '4':
                calc_sum_points()
            case '5':
                get_multiply_point()
            case 't':
                pass
            case 'q':
                break
            case _:
                print("Nie znaleziono takiej komendy ;O")
