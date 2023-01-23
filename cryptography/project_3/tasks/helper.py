def hex_to_bin(x):
    scale = 16
    num_of_bits = 8

    decimal = bin(int(x, scale))
    decimal_fill_zero = decimal[2:].zfill(num_of_bits)
    return decimal_fill_zero


def string_to_bin(x):
