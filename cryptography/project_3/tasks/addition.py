def add(x, y):
    return hex(int(x, 16) ^ int(y, 16))[2:]
