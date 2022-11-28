from .rand_elliptical_curve import rand_number_elliptic
from math import sqrt


def calc_elliptical_curve(a, b, p, x):
    return (x**3 + a * x + b) % p


def get_random_point(a, b, p):
    print("get_random_point")
    while True:
        x = rand_number_elliptic(p)
        fx0 = calc_elliptical_curve(a, b, p, x)

        if check_square_root():
            y = sqrt(fx0)
            return x, y

