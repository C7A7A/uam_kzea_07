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


def extended_euklides(a, b):
    x, y, u, v = 0, 1, 1, 0

    while a != 0:
        q = b // a
        r = b % a
        m = x - u * q
        n = y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n

    # b -> NWD
    # x, y -> a * x + b * y = b
    return b, x, y


if __name__ == '__main__':
    n = int(input("Podaj n: "))
    relatively_prime_numbers = create_rel_prime_numbers_group(n)
    print(relatively_prime_numbers)

    # print("GREAT_COMM_DIV")
    # print(greatest_common_divisor(8, 2))
    # print(greatest_common_divisor(21321, 321321))
    # print(greatest_common_divisor(360, 1))
    # print(greatest_common_divisor(2193219, 1024))
    #
    # print("EXT_EUK")
    # print(extended_euklides(100, 15))
    # print(extended_euklides(7919, 7873))



