from .rand_elliptical_curve import rand_number_elliptic
from cryptography.project_1.tasks.square_remainder import check_square_remainder
from cryptography.project_1.tasks.square_root import check_square_root
from cryptography.project_1.tasks.effective_exponentiation import binary_exponentiation


def calc_elliptical_curve(a, b, p, x):
    return (binary_exponentiation(x, 3, p) + a * x + b) % p


def get_random_point(a, b, p):
    print("--- GET RANDOM POINT ON ELLIPTICAL CURVE ---")

    while True:
        x = rand_number_elliptic(p)
        ellipse = calc_elliptical_curve(a, b, p, x)

        square_remainder = check_square_remainder(ellipse, p)
        if square_remainder:
            y = check_square_root(ellipse, p)
            print("x: {}, y: {}".format(x, y))
            return x, y

