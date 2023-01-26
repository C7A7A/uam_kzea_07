from ..project3 import hex_to_bin
from .xtime import xtime


def get_xtime_amount(y):
    return int(y, 16)


def multiply(x, y):
    xtime_amount = get_xtime_amount(y)
    # print("xtime_amount: ", xtime_amount)

    for i in range(xtime_amount):
        x = xtime(x)

    # print("final result: ", x)
    return x
