from tasks.calc_sum_points import calc_sum_points
from tasks.get_inverse_point import get_inverse_point
from tasks.get_multiply_point import get_multiply_point
from tasks.get_random_point import get_random_point
from tasks.rand_elliptical_curve import rand_elliptical_curve

if __name__ == '__main__':
    while True:
        p = int(input("Input p = 3 (mod 4): "))

        a, b = rand_elliptical_curve(p)
        x, y = get_random_point(a, b, p)
        print(x, y)
        # get_inverse_point()
        # calc_sum_points()
        # get_multiply_point()

    # while True:
        # description = """
        # 1. Wygeneruj losową krzywą eliptyczną
        # 2. Znajdź losowy punkt na krzywej
        # 3. Oblicz punkt przeciwny
        # 4. Oblicz PoQ sumę punktow krzywej eliptycznej
        # 5. Oblicz n-tą krotność punktu P
        #
        # q - zamknij program
        # """
        # print(description)
        # command = input('Podaj komendę: ')
