from .tasks.calc_sum_points import calc_sum_points
from .tasks.get_inverse_point import get_inverse_point
from .tasks.get_multiply_point import get_multiply_point
from .tasks.get_random_point import get_random_point
from .tasks.rand_elliptical_curve import rand_elliptical_curve


def start():
    while True:
        p = int(input("Input p = 3 (mod 4): "))

        a, b = rand_elliptical_curve(p)

        x1, y1 = get_random_point(a, b, p)
        x1, y1_inverse = get_inverse_point(x1, y1, p)
        x2, y2 = get_random_point(a, b, p)

        x3, y3 = calc_sum_points(x1, y1, x2, y2, a, p)
        # get_multiply_point()
