from ..project3 import hex_to_bin
from .xtime import xtime
from .addition import add


def get_xtime_amount(y_bin):
    y_bin_without_last_bit = y_bin[:-1]
    return int(y_bin_without_last_bit, 2)


def multiply(x, y):
    result = x
    y_bin = hex_to_bin(y)
    y_last_bit = y_bin[-1:]

    xtime_amount = get_xtime_amount(y_bin)
    # print("xtime_amount: ", xtime_amount)

    # xtime
    for i in range(xtime_amount):
        result = xtime(result)

    # xor with x (for example: (x^2 + 1)*(FF) = x^2*FF + FF)
    if y_last_bit == "1" and y != "01":
        result = add(result, x)

    # print("final result: ", x)
    return result
