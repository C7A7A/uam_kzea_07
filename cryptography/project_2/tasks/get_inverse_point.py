def calculate_inverse(y, p):
    return -y % p


def get_inverse_point(x, y, p):
    # print("--- GET INVERSE POINT ---")

    y_inverse = calculate_inverse(y, p)
    print("-P({}, {})".format(x, y_inverse))
    return x, y_inverse
