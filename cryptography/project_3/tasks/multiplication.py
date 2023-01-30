from ..project3 import hex_to_bin
from .xtime import xtime
from .addition import add


def get_bit_value(idx, bit):
    if bit == "1":
        return idx + 1
    return 0


def get_xtime_amount(y_bin):
    y_bin_without_last_bit = y_bin[:-1]
    y_bin_without_last_bit = y_bin_without_last_bit[::-1]

    x_times = [get_bit_value(idx, bit) for idx, bit in enumerate(y_bin_without_last_bit)]
    return x_times


def multiply(x, y):
    end_result = "00"
    y_bin = hex_to_bin(y)
    y_last_bit = y_bin[-1:]

    xtime_amount = get_xtime_amount(y_bin)
    print("xtime_amount: ", xtime_amount)

    # xtime
    for _, amount in enumerate(xtime_amount):
        xtime_result = x

        if amount != 0:
            # print("amount: ", amount)
            for _ in range(amount):
                xtime_result = xtime(xtime_result)
                # print("resutl: ", hex_to_bin(xtime_result))

            # print("after xtime:", result)
            end_result = add(xtime_result, end_result)
            # print("end result:", hex_to_bin(end_result))

    # xor with x (for example: (x^2 + 1)*(FF) = x^2*FF + FF)
    if y_last_bit == "1":
        if y != "01":
            end_result = add(x, end_result)
        else:
            end_result = x

    return end_result
