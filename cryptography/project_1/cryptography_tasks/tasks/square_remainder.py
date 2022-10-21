def check_square_remainder(a, p):
    pass


def square_remainder():
    print("--- SQUARE REMAINDER --- ")

    p = int(input("Enter p (must be prime): "))
    group_z_multiplication = [*range(0, p)]

    for num in group_z_multiplication:
        if check_square_remainder(num, p):
            print(f'{num} - reszta kwadratowa')
        else:
            print(f'{num} - nie jest resztą kwadratową')
