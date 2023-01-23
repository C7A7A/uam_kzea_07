from .helper import hex_to_bin


def xtime(x):
    ideal = hex_to_bin("1B")

    if x[0] == "0":
        x = int(x) << 1
        print(x)
    elif x[0] == "1":
        print("1 XD")
    else:
        print("ARGUMENT ERROR")
