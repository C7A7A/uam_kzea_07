from .effective_exponentiation import binary_exponentiation


def check_square_remainder(a, p):
    exp = int((p - 1) // 2)
    # (a**((p - 1) / 2)) mod p
    result = binary_exponentiation(a, exp, p)

    if result != -1:
        return True
    return False


def square_remainder():
    print("--- SQUARE REMAINDER --- ")

    p = int(input("Enter p (must be prime): "))
    # group_z_multiplication = [*range(0, p)]
    # print(f'group Z with multiplication: {group_z_multiplication}')

    b = int(input("Enter b: "))

    # if b not in group_z_multiplication:
    #     print('b not in group')
    #     return

    if check_square_remainder(b, p):
        print(f'{b} - reszta kwadratowa')

    # for num in group_z_multiplication:
    #     if check_square_remainder(num, p):
    #         print(f'{num} - reszta kwadratowa')
