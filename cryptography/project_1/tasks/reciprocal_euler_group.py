def greatest_common_divisor(a, b):
    if b == 0:
        return a

    return greatest_common_divisor(b, a % b)


def create_rel_prime_numbers_group(n):
    prime_nums = []

    for num in range(n):
        if greatest_common_divisor(num, n) == 1:
            prime_nums.append(num)

    return prime_nums


def extended_euklides(a, p):
    if a < 0:
        a = a + p

    start_p = p
    x, y, u, v = 0, 1, 1, 0

    while a != 0:
        q = p // a
        r = p % a
        m = x - u * q
        n = y - v * q
        p, a, x, y, u, v = a, r, u, v, m, n

    # b -> NWD
    # x, y -> a * x + b * y = b
    # return b, x, y
    return x % start_p


def reciprocal_euler_group():
    print("--- RECIPROCAL EULER GROUP ---")

    n = int(input("Enter n: "))
    b = int(input("Enter b: "))

    # reciprocal_num = (extended_euklides(b, n)[1]) % n
    reciprocal_num = extended_euklides(b, n)
    print(f'{b} - {reciprocal_num}')

    # for num in relatively_prime_numbers:
    #     reciprocal_num = (extended_euklides(num, n)[1]) % n
    #     print(f'{num} - {reciprocal_num}')
