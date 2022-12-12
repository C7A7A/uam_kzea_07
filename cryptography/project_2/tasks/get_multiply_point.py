from .calc_sum_points import calculate_same_points
from .calc_sum_points import calculate_different_points


def get_multiply_point(x1, y1, a, p, n):
    # print("--- MULTIPLY POINT N TIMES---")
    start_n = n

    x2 = x1
    y2 = y1
    x3, y3 = float("inf"), float("inf")

    while n > 0:
        if n % 2 == 1:
            x3, y3 = calculate_different_points(x3, y3, x2, y2, p)
            n = n - 1
        x2, y2 = calculate_same_points(x2, y2, a, p)
        n = n//2

    print("{} * ({}, {}) = ({}, {})".format(start_n, x1, y1, x3, y3))
    return x3, y3
