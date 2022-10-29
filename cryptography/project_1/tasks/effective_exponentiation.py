"""
calculate 2 ^ 3

START
result = 1
b = 2 = 10
k = 3 = 11

k is odd -> result = result * b = 1 * 2 = 2
b = b * b = 2 * 2 = 4
k = k / 2 = 01 = 1

k is odd -> result = 2 * 4 = 8
b = 8
k = 00 = 0

return result = 8
END
"""
def binary_exponentiation(b, k, n):
    """
    :param b: base
    :param k: exp
    :param n: mod n
    :return: b**k mod n
    """
    result = 1

    while k > 0:
        # if k is odd -> multiply result * b
        # k is odd when least significant bit is 1
        if (k & 1) == 1:
            # use modulo n to work on smaller numbers
            result = (result * b) % n

        b = (b * b) % n
        # k must be even -> k = k/2
        k = k >> 1

    return result


def effective_exponentiation():
    print("--- EFFECTIVE EXPONENTIATION ---")

    n = int(input("Enter n: "))
    group_z_multiplication = [*range(0, n)]
    print(f'group Z with multiplication: {group_z_multiplication}')

    k = int(input('Enter k: '))

    for num in group_z_multiplication:
        num_to_k = binary_exponentiation(num, k, n)
        print(f'{num} - {num_to_k}')
