from cryptography.project_1.tasks.reciprocal_euler_group import extended_euklides
from cryptography.project_1.tasks.effective_exponentiation import binary_exponentiation
from .get_inverse_point import calculate_inverse


def calculate_same_points(x1, y1, a, p):
    # lambd = ((3 * binary_exponentiation(x1, 2, p) + a) * extended_euklides((2 * y1) % p, p)) % p
    # x3 = (binary_exponentiation(lambd, 2, p) - (2 * x1) % p) % p
    # y3 = (lambd * (x1 - x3) - y1) % p

    lambd = (((3 * binary_exponentiation(x1, 2, p)) % p + a) * (extended_euklides((2 * y1) % p, p))) % p
    x3 = ((binary_exponentiation(lambd, 2, p) % p) - 2 * x1 % p) % p
    y3 = (lambd * (x1 - x3) - y1) % p

    return x3, y3


def calculate_different_points(x1, y1, x2, y2, p):
    # (x1, y1) is neutral element
    if x1 == float('inf') and y1 == float('inf'):
        x3 = x2
        y3 = y2
    # (x2, y2) is neutral element
    elif x2 == float('inf') and y2 == float('inf'):
        x3 = x1
        y3 = y1
    else:
        lambd = ((y2 - y1) * extended_euklides((x2 - x1), p)) % p
        # print(x2 - x1)
        # print(extended_euklides((x2 - x1), p))
        x3 = (binary_exponentiation(lambd, 2, p) - x1 - x2) % p
        y3 = (lambd * (x1 - x3) - y1) % p

    return x3, y3


# (P ⊕ Q) = O (neutral element)
def calculate_opposite_points():
    return float("inf"), float("inf")


def calc_sum_points(x1, y1, x2, y2, a, p):
    # print("--- CALCULATE SUM OF 2 POINTS (P ⊕ Q) ---")

    y1_inverse = calculate_inverse(y1, p)
    if x1 == x2 and y1_inverse == y2:
        x3, y3 = calculate_opposite_points()
    elif x1 == x2:
        x3, y3 = calculate_same_points(x1, y1, a, p)
    else:
        x3, y3 = calculate_different_points(x1, y1, x2, y2, p)

    print("({}, {}) + ({}, {}) = ({}, {})".format(x1, y1, x2, y2, x3, y3))
    return x3, y3
