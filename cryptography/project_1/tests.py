from tasks.reciprocal_euler_group import extended_euklides
from tasks.prime_number_fermat import fermat_primality_test
from tasks.effective_exponentiation import binary_exponentiation
from tasks.square_remainder import check_square_remainder
from tasks.square_root import check_square_root


def tests():
    # Zad 1
    assert (extended_euklides(3, 2 ** 30 - 5) == 357913940)
    assert (extended_euklides(100, 54321) == 10321)

    # Zad 2
    assert (binary_exponentiation(3, 2 ** 30, 2 ** 100 - 1) == 404294742055422617191248672231)
    assert (binary_exponentiation(10, 3 ** 39 + 1, 2 ** 62 + 10) == 1120803652654867934)

    # Zad 3
    assert (fermat_primality_test(2 ** 201 - 313, 100) is True)
    assert (fermat_primality_test(2 ** 201 - 323, 100) is False)
    assert (fermat_primality_test(2 ** 33 - 9, 100) is True)
    assert (fermat_primality_test(2 ** 33 - 21, 100) is False)

    # Zad 4
    assert (check_square_remainder(2, 2 ** 201 - 313) is True)
    assert (check_square_remainder(3, 2 ** 201 - 313) is False)
    assert (check_square_remainder(11, 2 ** 33 - 9) is True)
    assert (check_square_remainder(10, 2 ** 33 - 9) is False)

    # Zad 5
    assert (check_square_root(2, 2 ** 201 - 313) == 3101948484103482126970424634806781703628882321291710380824411)
    # assert (check_square_root(3, 2 ** 201 - 313) is False)
    assert (check_square_root(11, 2 ** 33 - 9) == 1578746474)
    # assert (check_square_root(10, 2 ** 33 - 9) is False)
