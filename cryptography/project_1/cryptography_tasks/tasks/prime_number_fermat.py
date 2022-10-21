import random
from .effective_exponentiation import binary_exponentiation


def fermat_primality_test(n, number_of_tests):
    if n <= 1 or n == 4:
        return False
    if n == 2 or n == 3:
        return True

    random_num = 0
    result = 0

    for _ in range(number_of_tests):
        random_num = random.randint(2, n - 2)

        result = binary_exponentiation(random_num, n - 1, n)
        # print(random_num, n, result)

        if result != 1:
            return False

    return True


def prime_number_fermat():
    print("--- PRIME NUMBER FERMAT ---")

    n = int(input("Enter n: "))
    k = int(input("How many tests: "))

    if fermat_primality_test(n, k):
        print(f'{n} - prime')
    else:
        print(f'{n} - not prime')
