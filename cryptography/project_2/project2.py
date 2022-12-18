import random

from .tasks.calc_sum_points import calc_sum_points
from .tasks.get_inverse_point import get_inverse_point
from .tasks.get_multiply_point import multiply_point
from .tasks.get_random_point import get_random_point
from .tasks.rand_elliptical_curve import rand_elliptical_curve
from random import randint
from cryptography.project_1.tasks.prime_number_fermat import fermat_primality_test


def rand_prime_for_elliptic_curve(bits):
    while True:
        num = 4 * random.getrandbits(bits) + 3
        if fermat_primality_test(num, 100):
            break
    return num


def start():
    # while True:
    # p = int(input("Input p = 3 (mod 4): "))
    # p = 523133468360889049404922330981983268743289535618129665870465316487757998439707462631766351
    # a = 230494833619330872742071433259892253887918924949625621075110348455162899582640562756609713
    # b = 225785530019760328737805254637561350820485164307786402015943227616074411698429350907607751

    p = rand_prime_for_elliptic_curve(1000)
    a, b = rand_elliptical_curve(p)
    # p = 11
    # a = 8
    # b = 1
    # x_alice = 3
    # x_bob = 5

    x1, y1 = get_random_point(a, b, p)
    # x1 = 5
    # y1 = 1
    x_alice = randint(0, p // 2)
    q1_alice, q2_alice = multiply_point(x1, y1, a, p, x_alice)

    x_bob = randint(0, p // 2)
    q1_bob, q2_bob = multiply_point(x1, y1, a, p, x_bob)

    s_alice = multiply_point(q1_bob, q2_bob, a, p, x_alice)
    s_bob = multiply_point(q1_alice, q2_alice, a, p, x_bob)

    print(s_alice, s_bob)
    if s_alice == s_bob:
        print("Points are equal")
    else:
        print("Points are not equal")
    # a, b = rand_elliptical_curve(p)
    # a = 1
    # b = 4

    # x1, y1 = get_random_point(a, b, p)
    # x1, y1_inverse = get_inverse_point(x1, y1, p)
    # x2, y2 = get_random_point(a, b, p)

    # x3, y3 = calc_sum_points(x1, y1, x2, y2, a, p)
    # x4, y4 = get_multiply_point(x1, y1, a, p, 10)
