from .effective_exponentiation import binary_exponentiation
from .square_remainder import check_square_remainder


def check_square_root(a, p):
    exp = int((p + 1) / 4)
    # (a**((p + 1) / 4)) mod p
    result = binary_exponentiation(a, exp, p)
    return result


def square_root():
    print("--- SQUARE ROOT ---")

    p = int(input("Enter p = 4k + 3: "))
    group_z_multiplication = [*range(0, p)]

    for num in group_z_multiplication:
        # check if num is square remainder of p
        if check_square_remainder(num, p):
            print(f'{num} - reszta kwadratowa')
            result = check_square_root(num, p)
            print(f'{result} - pierwiastek kwadratowy')
