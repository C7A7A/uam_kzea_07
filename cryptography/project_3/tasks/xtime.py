from .helper import hex_to_bin
from .addition import add


# TODO: to można zrobić na intach (wtedy >> i xor (^), ale trzeba odejmować 2^8 jak 1 na pierwszym bicie?
def xtime(x):
    ideal = "1B"
    x_bin = hex_to_bin(x)

    if x_bin[0] == "0":
        x_bin = x_bin[1:] + '0'
        result = hex(int(x_bin, 2))[2:]
    elif x_bin[0] == "1":
        # print("before: ", x_bin)
        x_bin = x_bin[1:] + '0'
        # print("after: ", x_bin)
        x = hex(int(x_bin, 2))

        # print("ideal: ", hex_to_bin(ideal))
        result = add(x, ideal)

    else:
        result = hex_to_bin("00")
        print("ARGUMENT ERROR")

    # print("xtime result: ", hex_to_bin(result))
    # print("xtime result: ", result)
    return result
