def hex_to_bin(x):
    scale = 16
    num_of_bits = 8

    binary = bin(int(x, scale))
    binary_fill_zero = binary[2:].zfill(num_of_bits)
    return binary_fill_zero
