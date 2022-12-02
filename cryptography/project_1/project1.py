from .tasks.reciprocal_euler_group import reciprocal_euler_group
from .tasks.prime_number_fermat import prime_number_fermat
from .tasks.effective_exponentiation import effective_exponentiation
from .tasks.square_remainder import square_remainder
from .tasks.square_root import square_root
from .tests import tests


def start():
    while True:
        description = """
        1. Odwrotność w grupie Funkcji φ (Eulera) z wykorzystaniem rozszerzonego algorytmu Euklidesa
        2. Algorytm efektywnego potęgowania w zbiorze Zn* z wykorzystaniem iterowanego podnoszenia do kwadratu
        3. Funkcja sprawdzająca czy liczba n jest liczbą pierwszą z wykorzystaniem testu Fermata
        4. Funkcja sprawdzająca czy element zbioru Zp* jest resztą kwadratową w Zp* z wykrozystaniem twierdzenia Eulera
        5. Funkcja która oblicza pierwiastek kwadratowy w φ(p) z wykorzystaniem twierdzenia Eulera

        q - zamknij program
        """
        print(description)
        command = input('Podaj komendę: ')

        match command:
            case '1':
                reciprocal_euler_group()
            case '2':
                effective_exponentiation()
            case '3':
                prime_number_fermat()
            case '4':
                square_remainder()
            case '5':
                square_root()
            case 't':
                tests()
            case 'q':
                break
            case _:
                print("Nie znaleziono takiej komendy ;O")