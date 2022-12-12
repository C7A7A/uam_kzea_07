from random import randint


def elliptic_delta(a, b, p):
    return (4 * a**3 + 27 * b**2) % p


def rand_number_elliptic(p):
    return randint(0, p - 1)


def rand_elliptical_curve(p):
    # print("--- GENERATE RANDOM ELLIPTICAL CURVE ---")

    while True:
        a = rand_number_elliptic(p)
        b = rand_number_elliptic(p)

        delta = elliptic_delta(a, b, p)
        if delta != 0:
            print("A: {} B: {} p: {}".format(a, b, p))
            return a, b
